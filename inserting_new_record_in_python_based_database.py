import sqlite3
MySchool=sqlite3.connect('schooltest.db')
curschool=MySchool.cursor()
curschool.execute("INSERT INTO student (StudentID, name, house, marks) VALUES (5,'Sherlock',32,50);")
MySchool.commit()
