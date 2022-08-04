# Author: Raul Varandela
# Date: 22/07/22
# Description: File that connect to the database and get the phase.

import sqlite3
import random
import os


# choosea ramdom function to use
def chooseFuctionTwitter():
    ramdomNumber = random.randint(1, 4)
    if ramdomNumber == 1:
        return getSkaterPhase()
    elif ramdomNumber == 2:
        return getPhase()
    elif ramdomNumber == 3:
        return getSetPhase()
    elif ramdomNumber == 4:
        return getFilosofyPhase()
    else:
        print("Error")


# choosea ramdom function to use
def chooseFuctionMastodon():
    ramdomNumber = random.randint(1, 3)
    if ramdomNumber == 1:
        return getFilosofyPhase()
    elif ramdomNumber == 2:
        return getPhase()
    elif ramdomNumber == 3:
        return getSetPhase()
    else:
        print("Error")


def connectToDB():
    con = sqlite3.connect('base de datos.db')
    cur = con.cursor()
    return cur


# get a skater phrase from the database
def getSkaterPhase():
    cur = connectToDB()
    for row in cur.execute('SELECT text FROM skate_tweets ORDER BY RANDOM() LIMIT 1;'):
        return row[0]


# get a ramdom phrase from the database
def getPhase():
    cur = connectToDB()
    for row in cur.execute('SELECT text FROM tweets ORDER BY RANDOM() LIMIT 1;'):
        return row[0]


# get a random set phrase from the database
def getSetPhase():
    cur = connectToDB()
    for row in cur.execute('SELECT text FROM frases_hechas ORDER BY RANDOM() LIMIT 1;'):
        return row[0]


# get a filosofy phrase from the database
def getFilosofyPhase():
    cur = connectToDB()
    for row in cur.execute('SELECT text FROM ifilosofia_tweets ORDER BY RANDOM() LIMIT 1;'):
        return row[0]


# choose a random image from the folder
def getPhoto():
    path = r"C:\\Users\\Raul\\Pictures\\TFM\\Insta"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    return f'C:\\Users\\Raul\\Pictures\\TFM\\Insta\\' + random_filename


# get a random reply from the database
def getReply():
    cur = connectToDB()
    for row in cur.execute('SELECT text FROM respuestas ORDER BY RANDOM() LIMIT 1;'):
        return row[0]
        

# get a random reply from the database
def getSimpleReply():
    cur = connectToDB()
    for row in cur.execute('SELECT text FROM simple_replies ORDER BY RANDOM() LIMIT 1;'):
        return row[0]


# get a phrase to use in a photo
def getDesciption():
    cur = connectToDB()
    for row in cur.execute('SELECT text FROM comentarios_fotos ORDER BY RANDOM() LIMIT 1;'):
        return row[0]