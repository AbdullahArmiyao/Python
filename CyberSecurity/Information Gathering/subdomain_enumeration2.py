#!/bin/python3

# To perform DNS lookup
import socket

# function to check url of fomat x.x.x
def check_url1(domain, subdomains, tld):
    # valid subdomain list
    found_subdomains = []
    # in the list of given subdomain
    for subdomain in subdomains:
        # in the list of given top domains
        for top in tld:
            try:
                # mkae valid url
                url = f"{subdomain}.{domain}.{top}"
                # obtain ip address
                ip_address = socket.gethostbyname(url)
                # if it checksout add it to the list
                found_subdomains.append(url)
                # print the result
                print(f"[+] Domain {url} found at {ip_address}")
            except socket.gaierror:
                # if url does not check out, skip
                print(f"[-] {url} not found")
                continue
            except Exception as e:
                # error handling
                print(f"[-] Error occurred with {url}: {str(e)}")
                continue
    return found_subdomains

# function to find domain of format x.x.x.x
def check_url(domain, subdomains, tld, tld2):
    found_subdomains = []
    for subdomain in subdomains:
        for top in tld:
            for top2 in tld2:
                try:
                    url = f"{subdomain}.{domain}.{top}.{top2}"
                    ip_address = socket.gethostbyname(url)
                    found_subdomains.append(url)
                    print(f"[+] Domain {url} found at {ip_address}")
                except socket.gaierror:
                    print(f"[-] {url} not found")
                    continue
                except Exception as e:
                    print(f"Error occured with {url}: {str(e)}")
                    continue
    return found_subdomains

# user inputs domain
domain = input("Enter domain name: ")
# modifyable list of subdomains and topdomains
subdomain = ["www", "elearning", "mail", "ftp", "test", "dev", "shop", "portal", "login", "secure", "dashboard", "vpn", "news", "webmail"]
topdomain = ["com", "vle", "net", "org", "edu", "gov", "mil", "io", "co", "us", "info", "biz", "tech", "dev", "ai", "shop", "site"]
topdomain2 = ["gh", "us", "uk", "de", "in", "au", "jp", "fr", "br", "ru", "it", "ca", "mx", "nl", "es", "za"]
# confirm number of TLDs
tld_count = int(input("How many top level domains?: "))
if tld_count == 1:
    found = check_url1(domain, subdomain, topdomain)
    print(f"Discovered domains: {found}")
elif tld_count == 2:
    found = check_url(domain, subdomain, topdomain, topdomain2)
    print(f"Discovered domains: {found}")

