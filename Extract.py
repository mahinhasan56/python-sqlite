import sqlite3
with sqlite3.connect("users.db") as db:
    cursor =db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user (userID INTEGER PRIMARY KEY,username VARCHAR(20) NOT NULL,
    firstname VARCHAR(20) NOT NULL, surname VARCHAR (20) NOT NULL, password VARCHAR(20)NOT NULL );''')

    cursor.execute("""INSERT INTO user (username,firstname,surname,password)VALUES("farukeu@gmail.com","Faruk","khan","12345")""")
    db.commit()


    cursor.execute("SELECT firstname , surname FROM user;")
    print(cursor.fetchall())

