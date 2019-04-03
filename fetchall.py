import sqlite3
MySchool=sqlite3.connect('schooltest.db')

sql="SELECT * from student;"
        
curschool=MySchool.cursor()
curschool.execute(sql)

result=curschool.fetchall()
for record in result:
    print (record)
