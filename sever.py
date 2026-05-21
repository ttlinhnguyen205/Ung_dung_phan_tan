import socket

def server_program():
    host = '127.0.0.1'
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))

    server_socket.listen(1)
    print("Server is waiting for client...")

    conn, address = server_socket.accept()
    print("Connected by:", address)

    while True:
        data = conn.recv(1024).decode()

        if not data:
            break

        print("Client:", data)

        if data.lower().strip() == "bye":
            print("Client disconnected.")
            break

        response = input("Server -> ")
        conn.send(response.encode())

    conn.close()
    server_socket.close()

if __name__ == '__main__':
    server_program()