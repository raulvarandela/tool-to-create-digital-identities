# Author: Raul Varandela
# Date: 22/07/22
# Description: File that connect to the database and get the phase.

import sqlite3

def getPhase():
    con = sqlite3.connect('base de datos.db')
    cur = con.cursor()
    for row in cur.execute('SELECT text FROM tweets ORDER BY RANDOM() LIMIT 1;'):
            return row[0]
