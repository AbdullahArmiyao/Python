import socket

# Create a function to scan for open ports
def scanner():
    ip_address = str(input("Enter a valid IP: "))
    
    for port in range(1, 1000):
        # IPv4 Addres with TCP connection
        obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Timeout after 5 secs
        obj.settimeout(0.1)
        # Port connection
        res = obj.connect_ex((ip_address, port))
        if res == 0:
            print(f"Port {port} is open")
        
    obj.close()


scanner()