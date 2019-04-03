import sqlite3
myschool=sqlite3.connect('new_database.db')
curschool=myschool.cursor()
curschool.execute('''CREATE TABLE student (
StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT (20) NOT NULL,
age INTEGER,
marks REAL);''')
myschool.close()
