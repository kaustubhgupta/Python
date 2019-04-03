import sqlite3
MySchool=sqlite3.connect('schooltest.db')
        
sql="SELECT * from student;"
        
curschool=MySchool.cursor()
curschool.execute(sql)
while True:
    record=curschool.fetchone()
    if record==None:
        break
    print (record)
