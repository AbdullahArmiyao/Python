import socket

# Enter the Server Address
# If it is over the internet and not the LAN, enter the public address of the server
# Use myip.is to check your public address\
host = str(input("Enter Server Address: "))
port = int(input("Enter Port Number: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

message = str(input("Message: "))
client.send(message.encode('utf-8'))
print(client.recv(1024))