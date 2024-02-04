"""
Завдання 2
Реалізуйте клієнт-серверний додаток з можливістю надсилати файли. Один користувач ініціює надсилання файлу, другий
підтверджує. Після підтвердження починається надсилання.
Якщо відправка була вдалою, повідомте про це відправника.
"""

#Серверний додаток (server.py)
import socket

def handle_client(client_socket):
    try:
        data = client_socket.recv(1024).decode('utf-8')
        if data == "send_file":
            client_socket.sendall("Send the file.".encode('utf-8'))
            filename = client_socket.recv(1024).decode('utf-8')
            with open(filename, 'wb') as f:
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    f.write(data)
            client_socket.sendall("File received successfully.".encode('utf-8'))
    except:
        pass
    finally:
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5555))
    server_socket.listen(1)

    print("Server started. Waiting for a client...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Client connected: {addr}")
        handle_client(client_socket)

main()

#Клієнтський додаток (client.py)
import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5555))

    file_to_send = input("Enter the filename to send: ")
    client_socket.sendall("send_file".encode('utf-8'))
    client_socket.recv(1024).decode('utf-8')
    client_socket.sendall(file_to_send.encode('utf-8'))

    with open(file_to_send, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            client_socket.sendall(data)

    print(client_socket.recv(1024).decode('utf-8'))

    client_socket.close()

main()
