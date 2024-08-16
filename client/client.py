import socket
import threading
from config import SERVER_HOST, SERVER_PORT, BUFFER_SIZE

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(BUFFER_SIZE).decode('utf-8')
            if message:
                print(f"Received: {message}")
        except:
            print("Connection lost")
            client_socket.close()
            break

def send_messages(client_socket):
    while True:
        message = input("Enter message: ")
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    send_messages(client_socket)
