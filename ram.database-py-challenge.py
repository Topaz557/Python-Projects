import sqlite3
from sqlite3 import Error


def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    conn = None;
    
    try:
        conn = sqlite3.connect(':memory:')
        c = conn.cursor()
            
        
        c.executescript("""DROP TABLE IF EXISTS Roster;\
                       CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT);\
                       INSERT INTO Roster VALUES('Jean-baptise Zorg', 'Human', 122);\
                       INSERT INTO Roster VALUES('Korben Dallas', 'Meat Popsicle', 100);\
                       INSERT INTO Roster VALUES('Ak not ', 'Mangalore', -5);""")


        c.executescript("""UPDATE Roster SET Species = 'Human' WHERE Species = 'Meat Popsicle'""")

        c.executescript("""SELECT Species from Roster WHERE Species = 'Human' """)
        y = c.fetchall()
        for row in y:
            print(row[0])

    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection()




                    


                
