import socket
import threading

# Set up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 55555))
server_socket.listen()

# List to store connected clients and their usernames
clients = {}

def handle_client(client_socket, client_address):
    # Get the client's username
    username = client_socket.recv(1024).decode()
    print(f"New connection from {client_address}: {username}")
    clients[client_socket] = username

    # Broadcast the new user to all clients
    broadcast(f"{username} has joined the chat")

    # Receive and broadcast messages from the client
    while True:
        try:
            message = client_socket.recv(1024).decode()
            broadcast(message)
        except:
            # Remove the client from the list of connected clients
            del clients[client_socket]
            broadcast(f"{username} has left the chat")
            break

    # Close the client socket
    client_socket.close()

def broadcast(message):
    for client_socket in clients:
        client_socket.send(message.encode())

# Listen for incoming connections and spawn a new thread to handle each one
while True:
    client_socket, client_address = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.start()
