import sqlite3
with sqlite3.connect("users.db") as db:
    cursor =db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user (userID INTEGER PRIMARY KEY,username VARCHAR(20) NOT NULL,
    firstname VARCHAR(20) NOT NULL, surname VARCHAR (20) NOT NULL, password VARCHAR(20)NOT NULL );''')
    cursor.execute("""INSERT INTO user (username,firstname,surname,password)VALUES("mahinhasan56@gmail.com","Faysal","Bin Hasan","12345")""")
    cursor.execute("""INSERT INTO user (username,firstname,surname,password)VALUES("masan56@gmail.com","GSon","Biswas","42345")""")
    cursor.execute("""INSERT INTO user (username,firstname,surname,password)VALUES("romel@gmail.com","Firuz","Zafor","42345")""")
    cursor.execute(
        """INSERT INTO user (username,firstname,surname,password)VALUES("masan56@gmail.com","Mehedi","Biswas","42345")""")
    cursor.execute(
        """INSERT INTO user (username,firstname,surname,password)VALUES("masan56@gmail.com","Hasan","Biswas","42345")""")
    db.commit()
    def newUser():
        found=0
        while found == 0:
            username = input("Please enter a username")
            with sqlite3.connect("users.db")as db:
                cursor=db.cursor()
                finduser = ("SELECT * FROM user WHERE username = ?")
                cursor.execute(finduser,[(username)])
        if cursor.fetchall():
                print("That User name  is already in use ,Please try again")
        else:
                found =1

                firstname =input("Please enter your first name:")
                surname= input("Please enter your surname:")
                password = input("Please enter a password")
                password1=input("Please enter your password again:")
                while password!=password:
                    print("Sorry Your password doesnot match please try again")
                    password =input("Please enter your password again:")
                    password1= input("Please enter your password again:")
                    insertData='''INSERT INTO user(username,firstname,surname,password) VALUES (?,?,?,?)'''
                    cursor.execute(insertData,[(username),(firstname),(surname),(password)])
                    db.commit()

                    newUser()
                    cursor.execute("SELECT * FROM user;")
                    print(cursor.fetchall())



