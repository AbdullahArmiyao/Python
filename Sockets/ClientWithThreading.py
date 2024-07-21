import socket
import threading

# Enter the Server Address
# If it is over the internet and not the LAN, enter the public address of the server
# Use myip.is to check your public address\
host = str(input("Enter Server Address: "))
port = int(input("Enter Port Number: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
username = input("Enter a username: ")

# Check to see if you received any message from server
# if it is a message of NICK, the client should enter his username
# The error message with the connection 
def receive():
    while True:
        try:
            message = client.recv(1024)
            if message == 'NICK':
                client.send(username.encode('ascii'))
            else:
                print(message)
        except:
            print("There was an error!")
            client.close()
            break

# Here's where the client gets to send messages
def write():
    while True:
        message = f"{username}: {input("")}"
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()