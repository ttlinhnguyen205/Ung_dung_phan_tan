from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

peer = xmlrpc.client.ServerProxy("http://localhost:9002", allow_none=True)

partial_result = 0

def compute_partial(numbers):
    global partial_result
    partial_result = sum([x**2 for x in numbers])
    print(f"[Worker1] Tổng bình phương phần 1: {partial_result}")
    peer.receive_partial_result(partial_result)
    return True

server = SimpleXMLRPCServer(("localhost", 9001), allow_none=True)
print("Worker1 đang chạy tại localhost:9001")

server.register_function(compute_partial, "compute_partial")
server.serve_forever()