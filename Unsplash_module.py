# Author: Raul Varandela
# Date: 10/08/22
# Get a random photo from Unsplash API

import hashlib
import requests, random, shutil, os
import DB_connect
import os


# get a random photo from Unsplash API
def getPhoto(rrss):
    page = 1
    i = 0
    request = requests.get(f'https://api.unsplash.com/search/photos/?query=skate&client_id=p3bC3AHbsXuo_X89P_V4gSe6x2xcX2n9zAy6CN1C2HY&page={page}&per_page=30').json()
    randomNumber = random.randint(0, 29)

    condiction = True

    while condiction:

        if i == 29:
            page += 1
            i = 0
            request = requests.get(f'https://api.unsplash.com/search/photos/?query=skate&client_id=p3bC3AHbsXuo_X89P_V4gSe6x2xcX2n9zAy6CN1C2HY&page={page}&per_page=30').json()

        photo = request.get('results')[randomNumber]
        res = requests.get(photo.get('urls').get('full'), stream = True)
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        file_name = f'{BASE_DIR}/media/{photo.get("id")}.jpg'
       
        if res.status_code == 200:
            with open(file_name,'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ',file_name)
        else:
            print('Image Couldn\'t be retrieved')
        
        if checkHash(calculateHash(file_name), rrss):
            deletePhoto(file_name)
            randomNumber = random.randint(0, 29)
            i += 1
        else:
            condiction = False
            DB_connect.addHash(calculateHash(file_name), rrss)
            return file_name



# delete a photo from media folder
def deletePhoto(file_name):
     os.remove(file_name)


# calculate the hash of a photo
def calculateHash(file_name):
    return hashlib.sha256(open(file_name, 'rb').read()).hexdigest()


# check if the hash's photo is already in the database
def checkHash(hash, rrss):
    if DB_connect.getHash(hash, rrss):
        return True
    else:
        return False