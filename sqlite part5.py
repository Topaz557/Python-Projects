import sqlite3

#get person data from ser
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))

#Execute insert statement from supplied person data
with sqlite3.connect("C:/Users/andre/Documents/GitHub/Python-Projects/test_database.db")as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES ('"+ firstName +"', '"+ lastName +"', " +str(age) +")"
    c.execute(line)
