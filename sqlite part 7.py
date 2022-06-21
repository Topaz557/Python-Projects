import sqlite3

peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

with sqlite3.connect("C:/Users/andre/Documents/GitHub/Python-Projects/test_database.db")as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, age INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)",
                  peopleValues)

#select all first and last named from people over age 30
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    for row in c.fetchall():
        print (row)
