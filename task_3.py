"""
Завдання 3
Реалізуйте клієнт-серверний додаток , який дозволяє
користувачам спілкуватися в одному чаті. Кожен користувач
входить у чат під своїм логіном та паролем. Повідомлення,
надіслане в чат, видно всім користувачам чату.
"""
#Серверний додаток (server.py):
import socket
import threading

clients = {}
addresses = {}

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if data.startswith("login"):
                username = data.split(":")[1]
                password = data.split(":")[2]
                clients[username] = client_socket
                print(f"User {username} logged in.")
                broadcast(f"{username} has joined the chat.")
            elif data == "quit":
                client_socket.close()
                print(f"User {username} logged out.")
                del clients[username]
                broadcast(f"{username} has left the chat.")
                break
            else:
                broadcast(data)
        except:
            break

def broadcast(message):
    for client in clients.values():
        client.sendall(message.encode('utf-8'))

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5555))
    server_socket.listen(5)

    print("Server started. Waiting for clients...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Client connected: {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

main()

#Клієнтський додаток (client.py)
import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5555))

    username = input("Enter your username: ")
    password = input("Enter your password: ")
    client_socket.sendall(f"login:{username}:{password}".encode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        if message == "quit":
            client_socket.sendall(message.encode('utf-8'))
            break
        else:
            client_socket.sendall(message.encode('utf-8'))

    client_socket.close()

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            print(data)
        except:
            break

main()
