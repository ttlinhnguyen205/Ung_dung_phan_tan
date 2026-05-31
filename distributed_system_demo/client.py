import xmlrpc.client

coordinator = xmlrpc.client.ServerProxy("http://localhost:8000", allow_none=True)

numbers = list(range(1, 11))  # [1..10]

print("[Client] Gửi dữ liệu tới Coordinator...")
total = coordinator.run_distributed_sum(numbers)
print(f"[Client] Kết quả tổng bình phương là: {total}")