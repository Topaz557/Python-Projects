import os
import sqlite3
conn = sqlite3.connect('test5.db')
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )")
    for file in fileList:
        if file.endswith('.txt'):
            cur.execute("INSERT INTO tbl_persons (col_fname) VALUES (?)",(file,))
            print(file)
    conn.commit()
conn.close()

