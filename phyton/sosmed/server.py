import socket
import threading
import json

HOST = "127.0.0.1"
PORT = 52128

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

users = {}
posts = []

def handle_client(client_socket):
    global posts
    while True:
        try:
            data = client_socket.recv(4096).decode()
            if not data:
                break
            request = json.loads(data)
            action = request.get("action")

            if action == "signup":
                username = request.get("username")
                if username and username not in users:
                    users[username] = []
                    response = {"message": "Signup successful"}
                else:
                    response = {"message": "Username already taken"}

            elif action == "post":
                username = request.get("username")
                text = request.get("text")
                if username in users and text:
                    posts.append({"username": username, "text": text, "likes": 0})
                    response = {"message": "Post successful"}
                else:
                    response = {"message": "Invalid post"}

            elif action == "like":
                post_index = request.get("post_index")
                if 0 <= post_index < len(posts):
                    posts[post_index]["likes"] += 1
                    response = {"message": "Post liked"}
                else:
                    response = {"message": "Invalid post index"}

            elif action == "get_posts":
                response = posts

            else:
                response = {"message": "Invalid action"}

            client_socket.send(json.dumps(response).encode())
        except:
            break
    client_socket.close()

def start_server():
    print(f"Server listening on {HOST}:{PORT}")
    while True:
        client, addr = server.accept()
        print(f"New connection from {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client,))
        client_thread.start()

if __name__ == "__main__":
    start_server()