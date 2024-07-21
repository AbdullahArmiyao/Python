import socket
import threading

# Specifying a host to make clear it is a server
# host = socket.gethostbyname(socket.gethostname())
port = int(input("Enter a valid port number: "))

# Creating the socket with 2 properties
# Address type, Protocol
# AF_INET = IPv4, AF_INET6 = IPv6
# SOCK_STREAM = TCP, SOCK_DGRAM = UDP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the IP and Port 
server.bind(('', port))
# Now listen to incoming connections
# The integer is sort of a limit to the number of unaccepted connections
server.listen()

# List of clients and their usernames
clients = []
usernames = []

# Delivering the message to everyone on the server
def broadcast(message):
    for client in clients:
        client.send(message)

# Check if client messages go through
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            # if messages cannot be broadcasted, remove the user because the user lost connection
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames(index)
            broadcast(f"{username} left the chat".encode('utf-8'))
            usernames.remove(username)
            break

# Check if connection sucessful
# if successful, Ask for a username
# Append the username and client to the respective lists
# Broadcast a message to alert everyone
# start a messaging thread
def receive():
    while True:
        client, address = server.accept()
        print(f"Connection with {str(address)} successful")

        client.send('NICK'.encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client)

        print(f"Username of client is {username}")
        broadcast(f"{username} just joined the party\n".encode('utf-8'))
        client.send("Connected to server".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server listening...")
receive()