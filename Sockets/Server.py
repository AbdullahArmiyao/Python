import socket

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
server.listen(5)

while True:
    # Returns address of client and socket to talk to client
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    # receive message and decode them since it's encoded upon sending
    message = communication_socket.recv(1024).decode('utf-8')
    # Print the message
    print(f"{address}: {message}")
    out = str("Hello")
    # The message must always be encoded
    communication_socket.send(f"{out}".encode('utf-8'))
    # You can close the connection if you no longer have any message
    communication_socket.close()
    print("Connection closed")