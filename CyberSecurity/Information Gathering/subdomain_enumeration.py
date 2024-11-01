#!/bin/python3

# import socket to perform DNS Lookup
import socket

# function to find which subdomain exists subdomain
def check_subdomain(domain, subdomains):
    # list of available subdomains
    found_subdomains = []
    for subdomain in subdomains:
        try:
            # create a full url
            full_domain = f"{subdomain}.{domain}"
            # Get the domain name and IP by using DNS
            ip_address = socket.gethostbyname(full_domain)
            # Add the url to the domain and print it
            found_subdomains.append(full_domain)
            print(f"Found {full_domain} at {ip_address}")
        # If the DNS fails, ignore
        except socket.gaierror:
            print(f"{full_domain} not found")
            continue
    return found_subdomains


    
domain = input("Enter Target domain: ")
subdomains = ["www", "mail", "ftp", "test", "dev", "shop", "portal", "login", "secure", "dashboard", "vpn", "news", "webmail"]
found = check_subdomain(domain, subdomains)
print(f"Discovered domains: {found}")