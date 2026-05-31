from xmlrpc.server import SimpleXMLRPCServer

data_part = []
peer_partial_result = 0

def set_data(numbers):
    global data_part
    data_part = numbers
    print(f"[Worker2] Nhận phần dữ liệu 2: {data_part}")
    return True

def receive_partial_result(value):
    global peer_partial_result
    peer_partial_result = value
    print(f"[Worker2] Nhận kết quả từ Worker1: {value}")
    return True

def final_result():
    local_result = sum([x**2 for x in data_part])
    total = local_result + peer_partial_result
    print(f"[Worker2] Tổng toàn bộ: {total}")
    return total

server = SimpleXMLRPCServer(("localhost", 9002), allow_none=True)
print("Worker2 đang chạy tại localhost:9002")

server.register_function(set_data, "set_data")
server.register_function(receive_partial_result, "receive_partial_result")
server.register_function(final_result, "final_result")
server.serve_forever()