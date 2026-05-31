from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

worker_info = {
    "worker1": ("localhost", 9001),
    "worker2": ("localhost", 9002)
}

# Kết nối tới các worker
worker1 = xmlrpc.client.ServerProxy(f"http://{worker_info['worker1'][0]}:{worker_info['worker1'][1]}", allow_none=True)
worker2 = xmlrpc.client.ServerProxy(f"http://{worker_info['worker2'][0]}:{worker_info['worker2'][1]}", allow_none=True)

def run_distributed_sum(numbers):
    half = len(numbers) // 2
    part1 = numbers[:half]
    part2 = numbers[half:]

    print("[Coordinator] Gửi phần 1 tới Worker1")
    worker1.compute_partial(part1)

    print("[Coordinator] Gửi phần 2 tới Worker2")
    worker2.set_data(part2)

    print("[Coordinator] Nhận kết quả tổng từ Worker2")
    total = worker2.final_result()
    return total

server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
print("Coordinator đang chạy tại localhost:8000")

server.register_function(run_distributed_sum, "run_distributed_sum")
server.serve_forever()