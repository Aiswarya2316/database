import sqlite3
con =sqlite3.connect("sample.db")
try:
    con.execute("create table student(age int,name text,mark real)")
except:
    pass
con.execute("insert into student(age,name,mark)values(25,'anu',100)") 
con.commit()   
