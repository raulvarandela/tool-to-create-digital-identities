# Author: Raul Varandela
# Date: 30/07/22
# Description: Test Main file for the project.

import shutil
from urllib import request
import requests
import twitter, mastodon_app, instagram, Unsplash_module,DB_connect
import datetime
from bs4 import BeautifulSoup

import time
import string
import random

'''


def username_gen(length=24, chars= string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(length))  

def password_gen(length=8, chars= string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(length)) 


print(username_gen())
print(password_gen())


username = username_gen()
password = password_gen()
domain = 'bukhariansiddur.com'

url = "https://api.mail.gw/accounts"
payload = {
    "address": f"{username}@{domain}",
    "password": password
}
headers = { 'Content-Type': 'application/json' }

data = requests.post(url, headers=headers, json=payload).json()
print(data)
print("----------------------------------------------------")

url = "https://api.mail.gw/token"
payload = {
    "address": data["address"] ,
    "password": password
}
headers = { 'Content-Type': 'application/json' }
data = requests.post(url, headers=headers, json=payload).json()        
print(data["token"])
token = data["token"]
print("----------------------------------------------------")


url = "https://api.mail.gw/messages"
payload = {
    "Authorization": token 
}
headers = { 'Content-Type': 'application/json' }
data = requests.get(url, headers=headers, json=payload).json()
print(data)
print("----------------------------------------------------")

url = f"https://api.mail.gw/accounts/{data['id']}"
payload = {
    "Authorization": data["token"] 
}
headers = { 'Content-Type': 'application/json' }
data = requests.delete(url, headers=headers, json=payload).json()
print(data)
print("----------------------------------------------------")'''

mastodon_app.createAccount()




