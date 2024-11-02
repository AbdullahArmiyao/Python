'''---------------PORT SCANNER-----------------
How it works:
User enters target IP address. Then the IP address
is bound to each port from 1 to the limit given.
A connection to the address is done for every
port and if there's a connection, it means the
port is open.
-----------------------------------------------'''

import socket

# Create a function to scan for open ports
def scanner():
    ip_address = str(input("Enter a valid IP: "))
    contype = int(input("What kind of scan?\n1. TCP\t2. UDP\t3.Both:\t"))
    
    for port in range(1, 1000):
        if contype == 1 or contype == 3:
            # IPv4 Addres with TCP connection
            obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Timeout after 5 secs
            obj.settimeout(0.1)
            # Port connection
            res = obj.connect_ex((ip_address, port))
            if res == 0:
                print(f"Port TCP/{port} is open")
        elif contype == 2 or contype == 3:
            # IPv4 Address with UDP connection
            obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            obj.settimeout(0.1)
            try:
                # send empty UDP datagram
                obj.sendto(b'',  (ip_address, port))
                obj.recvfrom(1024)
                print(f"Port UDP/{port} might be open")
            except socket.error as e:
                if "Permission Denied" in str(e):
                    print(f"Permisson Denied for port {port}")
                elif "Network is unreachable" in str(e):
                    print(f"Port UDP/{port} is not reachable")
                elif isinstance(e, socket.timeout):
                    print(f"Port UDP/{port} is likely closed")
                else:
                    if "Connection refused" in str(e):
                        print(f"Port UDP/{port} is filtered/blocked")
                    else:
                        print(f"Port UDP/{port} is likely closed")
       
            
    obj.close()


scanner()