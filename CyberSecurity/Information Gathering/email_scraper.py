#!/bin/python3

# import regex for email pattern matches
import re
# import requests to fetch web contents
import requests
# import beautifilsoap to parse html
from bs4 import BeautifulSoup

def email_scraper(url):
    emails = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        emails = re.findall(r'[a-zA-Z0-9._+%-]+@[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,}', str(soup))
    except requests.RequestException as e:
        print(f"Error fetching {url}:{str(e)}")
        return emails
    

url = input("Enter URL: ")
emails = email_scraper(url)
print(f"Available Emails: {emails}")