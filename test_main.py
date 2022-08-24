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
import re


'''

def username_gen(length=24, chars= string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(length))  

def password_gen(length=8, chars= string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(length)) 

username = username_gen()
password = password_gen()
domain = 'bukhariansiddur.com'




print(f'Usuario:    {username}@bukhariansiddur.com')
print(f'Password:   {password}')


# crear el usuario
url = "https://api.mail.gw/accounts"
payload = {
    "address": f"{username}@{domain}",
    "password": password
}
headers = { 'Content-Type': 'application/json' }
data = requests.post(url, headers=headers, json=payload).json()
print(data)
print("----------------------------------------------------")

# conseguir el token
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

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2NjEzNTQ1OTIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJ1c2VybmFtZSI6ImduMWZ3Y2JhdTNhcWR5ODZoNmZ2aHpyMEBidWtoYXJpYW5zaWRkdXIuY29tIiwiaWQiOiI2MzA2NDI1ZjQxZThmNjRiOTg0ZjQwZjMiLCJtZXJjdXJlIjp7InN1YnNjcmliZSI6WyIvYWNjb3VudHMvNjMwNjQyNWY0MWU4ZjY0Yjk4NGY0MGYzIl19fQ.dwU_LBgKT6sXqCKCsfqiOOb_XxxyinSryHLIgijjtfPB8Rhm4J1WenWhwjn6KOPHK04oDpvil4EobzTxdQmuWA'

#aaceder a los mensajes
url = "https://api.mail.gw/messages"
payload = {
    "Authorization": token 
}
headers = { 'Authorization': 'Bearer ' + token }
data = requests.get(url, headers=headers, json=payload).json()
print(data)
print("----------------------------------------------------")

print(data['hydra:totalItems'])





url = f"https://api.mail.gw/messages/{data['hydra:member'][0]['id']}"
payload = {
    "Authorization": token 
}
headers = { 'Authorization': 'Bearer ' + token }
data = requests.get(url, headers=headers, json=payload).json()
print(data)
print("----------------------------------------------------")



num = re.findall("https://[a-z.]+/auth/confirmation\?confirmation_token=[a-zA-Z0-9_-]+&redirect_to_app=true", data['text'])
print(str(num[0]))
#print(requests.get(num[0]).json)

'''


print(mastodon_app.createAccount())