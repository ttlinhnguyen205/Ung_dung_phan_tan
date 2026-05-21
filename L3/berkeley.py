import random

def berkeley_algorithm(num_slaves, master_time, min_offset, max_offset):
    print("--- Khởi tạo Thuật toán Berkeley ---")
    print(f"[Master] Thời gian gốc: {master_time}s")
    print(f"Giả lập độ lệch thời gian ngẫu nhiên so với Master (từ {min_offset} đến {max_offset} giây).")
    print()

    offsets = []
    slave_times = []

    print("--- Giai đoạn Thăm dò (Polling) ---")

    for i in range(num_slaves):
        offset = random.randint(min_offset, max_offset)
        slave_time = master_time + offset

        offsets.append(offset)
        slave_times.append(slave_time)

        print(f"[Slave {i + 1}] Độ lệch: {offset:+d}s | Thời gian: {slave_time}s")

    total_offset = sum(offsets)
    average_offset = total_offset / (num_slaves + 1)

    print()
    print(f"[Master] Tổng độ lệch: {total_offset:+d}s")
    print(f"[Master] Độ lệch trung bình cần điều chỉnh: {average_offset:.2f}s")
    print()

    print("--- Giai đoạn Đồng bộ (Adjustment) ---")

    synchronized_time = master_time + average_offset
    print(f"[Master] Thời gian đã đồng bộ: {synchronized_time:.2f}s")

    for i in range(num_slaves):
        adjustment = average_offset - offsets[i]
        new_time = slave_times[i] + adjustment

        print(f"[Slave {i + 1}] Điều chỉnh: {adjustment:+.2f}s | Thời gian mới: {new_time:.2f}s")


# ===== THAY THÔNG SỐ Ở ĐÂY =====
berkeley_algorithm(
    num_slaves=5,
    master_time=100,
    min_offset=-5,
    max_offset=5
)