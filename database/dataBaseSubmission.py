import os ## Here I am importing the Operating system so the sqlite and python can interact
import sqlite3## here I am importing the sqlite so that it may interact with python/os system
conn = sqlite3.connect('test5.db')## Here I am connecting to sequel
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')## here I am assining a tupple for file list


with conn:
    cur = conn.cursor() ## here I am assinging cur as the conn cursor for ease of operation
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )") ## here I am telling the cursor to execute creating a table if there is not already one, as well as a field/column
    for file in fileList: ## here I am starting a for startment that will loop through my files
        if file.endswith('.txt'): ## here I am telling the system to only recognize the files ending in .txt
            cur.execute("INSERT INTO tbl_persons (col_fname) VALUES (?)",(file,)) ## here I am telling python to pull the txt files and to insert their names into the fname table
            print(file) ## here I am printing the files ending in txt to ensure we are properly connecting
    conn.commit() ## here I am commiting the changes to sql
conn.close() ## here I am closing out sql

