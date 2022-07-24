import sqlite3

def getPhase():
    con = sqlite3.connect('base de datos.db')
    cur = con.cursor()
    for row in cur.execute('SELECT * FROM BD ORDER BY RANDOM() LIMIT 1;'):
            return row[0]
