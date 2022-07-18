import os
import sqlite3
conn = sqlite3.connect('test3.db')
horse = ('andrew.txt')


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )")
    for file in horse:
        if file.endswith('.txt'):
            cur.execute("INSERT INTO tbl_persons (col_fname) VALUES (?)",(file,))
            print(file)
    conn.commit()
conn.close()

