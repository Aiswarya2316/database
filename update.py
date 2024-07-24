import sqlite3

con = sqlite3.connect("sample.db")#db connection

try:
    con.execute("create table student(age int,name text,mark real)")#create table
except:
    pass

# con.execute("update student set name='m....' where name='anu'")
# con.commit
name=str(input("enter ur name:"))
new=str(input("new name:"))
con.execute("update student set name=? where name=?",(new,name))
con.commit
data=con.execute("select * from student")
print("{:<15}{:<15}{:<15}".format("age","name","mark"))
print('_'*45)
for i in data:
    print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2])) 
print()