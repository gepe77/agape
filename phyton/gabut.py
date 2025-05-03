import openai

import socket
import threading

# Konfigurasi server
HOST = '127.0.0.1'  # Localhost
PORT = 5000         # Port untuk server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message, client)
        except:
            clients.remove(client)
            break

def receive_connections():
    print("Server berjalan di port", PORT)
    while True:
        client, addr = server.accept()
        print(f"Terhubung dengan {addr}")
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_connections()

# Client script (untuk dijalankan secara terpisah)
def client_program():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    
    def receive_messages():
        while True:
            try:
                message = client.recv(1024).decode()
                print(message)
            except:
                break
    
    threading.Thread(target=receive_messages, daemon=True).start()
    
    while True:
        message = input()
        if message.lower() == 'exit':
            break
        client.send(message.encode())
    client.close()

# Jalankan `client_program()` di file terpisah untuk mencoba chat