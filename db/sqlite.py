import sqlite3 as sq

with sq.connect('example.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (userid INT PRIMARY KEY, name TEXT, old INTEGER, grup INTEGER)""")
con.commit








