import sqlite3

#get person data from ser
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)

#Execute insert statement from supplied person data
with sqlite3.connect("C:/Users/andre/Documents/GitHub/Python-Projects/test_database.db")as connection:
    c = connection.cursor()   
    c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)
    c.execute("Update People SET age=? WHERE FirstName=? and LastName=?",
          (45, 'Luigi', 'Vercotti'))
