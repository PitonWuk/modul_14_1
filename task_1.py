"""
Завдання 1
Реалізуйте клієнт-серверний додаток, що дозволяє двом
користувачам грати в гру «Хрестики — нулики». Один із
гравців ініціює гру. Якщо другий гравець підтверджує, то
гра починається. Гру можна припинити. Той хто припинив
гру — програв. Після завершення гри можна ініціювати повторний матч.

"""
#Серверний додаток (server.py)
import socket
import threading


def handle_client(client_socket, clients):
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Received: {data}")

            if data == "start":
                client_socket.sendall("Waiting for the second player...".encode('utf-8'))
                clients.append(client_socket)
            elif data == "confirm":
                if len(clients) == 2:
                    client_socket.sendall("Game started!".encode('utf-8'))
                    other_client = clients[1] if client_socket == clients[0] else clients[0]
                    other_client.sendall("Game started!".encode('utf-8'))
                else:
                    client_socket.sendall("Waiting for another player to confirm...".encode('utf-8'))
            elif data == "quit":
                client_socket.sendall("Game over. You lose.".encode('utf-8'))
                clients.remove(client_socket)
            else:
                other_client = clients[1] if client_socket == clients[0] else clients[0]
                other_client.sendall(data.encode('utf-8'))
    except:
        pass
    finally:
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5555))
    server_socket.listen(2)

    clients = []
    print("Server started. Waiting for clients...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Client connected: {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, clients))
        client_handler.start()

main()

#Клієнтський додаток (client.py)
import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5555))

    while True:
        message = input("Enter 'start' to initiate the game, 'confirm' to confirm the game, 'quit' to quit the game, or your move (e.g., 'X1' or 'O2'): ")
        client_socket.sendall(message.encode('utf-8'))

        if message == "quit":
            break

        data = client_socket.recv(1024).decode('utf-8')
        print("Server:", data)

    client_socket.close()

main()

