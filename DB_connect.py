# Author: Raul Varandela
# Date: 22/07/22
# Description: File that connect to the database and get the phase.

import sqlite3
import os.path


# connect to the database
def connectToDB():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, 'base de datos.db')
    con = sqlite3.connect(db_path)
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


# check if the hash is already in the database
def getHash(hash, rrss):
    cur = connectToDB()
    for row in cur.execute(f'SELECT hash FROM hashs_photos WHERE hash = "{hash}" AND RRSS = "{rrss}";'):
        return row[0]


# add a hash to the database
def addHash(hash,rrss):
    cur = connectToDB()
    cur.execute(f'INSERT INTO hashs_photos(hash,RRSS) VALUES ("{hash}","{rrss}");')
    cur.connection.commit()


#get last date from the database
def getLastDate(rrss):
    cur = connectToDB()
    for row in cur.execute(f'SELECT date FROM comments_date WHERE RRSS = "{rrss}";'):
        return row[0]


# add a date to the database
def addDate(date,rrss):
    cur = connectToDB()
    cur.execute(f'UPDATE comments_date SET date = "{date}" WHERE RRSS = "{rrss}";')
    cur.connection.commit()


# add a user to the database
def addUser(username,email,passwd,token):
    cur = connectToDB()
    cur.execute(f'INSERT INTO mastodon_accounts(username,mail,passwd,token) VALUES ("{username}","{email}","{passwd}","{token}");')
    cur.connection.commit()