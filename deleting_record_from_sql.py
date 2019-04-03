import sqlite3
MySchool=sqlite3.connect('schooltest.db')
            
nm=input("enter name: ")
sql="SELECT * from student WHERE name='"+nm+"';"
curschool=MySchool.cursor()
curschool.execute(sql)
record=curschool.fetchone()
print (record)
res=input("Do you want to delete this record (Y/N)")
sql="DELETE FROM student WHERE name='"+nm+"';"
if res=='Y':
    try:
        curschool.execute(sql)
        MySchool.commit()
        print ("record updated successfully")
    except:
        print ("error in update operation")
        MySchool.rollback()
        

