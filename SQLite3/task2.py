import sqlite3
con =sqlite3.connect("sample.db")
try:
    con.execute("create table student(age int,name text,mark real)")
except:
    pass
age=int(input("age"))
name=str(input("name"))
mark=int(input("mark"))

con.execute("insert into student(age,name,mark)values(?,?,?)",(age,name,mark)) 
con.commit()   
