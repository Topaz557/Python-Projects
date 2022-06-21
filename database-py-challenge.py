import sqlite3
from sqlite3 import Error


def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    conn = None;
    
    try:
        conn = sqlite3.connect(':memory:')
        conn.executescript("""DROP TABLE IF EXISTS Roster;\
                       CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT);\
                       INSERT INTO Roster VALUES('Jean-baptise Zorg', 'Human', 122);\
                       INSERT INTO Roster VALUES('Korben Dallas', 'Meat Popsicle', 100);\
                       INSERT INTO Roster VALUES('Ak not Mangalore', 'Human', 122);""")
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection()



                    


                
