#!/bin/python3

'''-----------------------Domain IP Finder----------------------
How it works:
The user enters a valid URL, then the code tries to obtain the IP
by finding the domain. As long as the domain is valid, it most 
definetly has an IP.
(This is the simplest explanation I could give...)
----------------------------------------------------------------'''


# import socket
import socket

# main function to find domain ip address
def find_ip():
    # user input for URL
    domain = input("Enter URL: ")
    try:
        # Get the ip address of the url
        ip_address = socket.gethostbyname(domain)
        # Print the IP 
        print(f"The ip for \"{domain}\" is {ip_address}")
    except socket.gaierror:
        # incase the domain does not exist
        print("Domain doesn't exit. IP not found...")
    except Exception as e:
        # debug purposes
        print(str(e))

find_ip()