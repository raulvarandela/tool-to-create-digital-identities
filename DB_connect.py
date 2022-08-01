# Author: Raul Varandela
# Date: 22/07/22
# Description: File that connect to the database and get the phase.

import sqlite3
import random
import os


def chooseFuctionTwitter():
    ramdomNumber = random.randint(1,4)
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


def chooseFuctionMastodon():
    ramdomNumber = random.randint(1,3)
    if ramdomNumber == 1:
        return getFilosofyPhase()
    elif ramdomNumber == 2:
        return getPhase()
    elif ramdomNumber == 3:
        return getSetPhase()
    else:
        print("Error")


def getSkaterPhase():
    con = sqlite3.connect('base de datos.db')
    cur = con.cursor()
    for row in cur.execute('SELECT text FROM skate_tweets ORDER BY RANDOM() LIMIT 1;'):
        return row[0]


def getPhase():
    con = sqlite3.connect('base de datos.db')
    cur = con.cursor()
    for row in cur.execute('SELECT text FROM tweets ORDER BY RANDOM() LIMIT 1;'):
        return row[0]


def getSetPhase():
    con = sqlite3.connect('base de datos.db')
    cur = con.cursor()
    for row in cur.execute('SELECT text FROM frases_hechas ORDER BY RANDOM() LIMIT 1;'):
        return row[0]


def getFilosofyPhase():
    con = sqlite3.connect('base de datos.db')
    cur = con.cursor()
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

def getReply():
    con = sqlite3.connect('base de datos.db')
    cur = con.cursor()
    for row in cur.execute('SELECT text FROM respuestas ORDER BY RANDOM() LIMIT 1;'):
        return row[0]