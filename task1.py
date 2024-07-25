import sqlite3
con =sqlite3.connect("sample.db")
try:
    con.execute("create table student(age int,name text,mark real)")
except:
    pass
# con.execute("insert into student(age,name,mark)values(25,'anu',100)") 
# con.commit()   

# data=con.execute("select * from student where name like'_i%'")
# print("{:<15}{:<15}{:<15}".format("age","name","mark"))
# print('_'*45)
# for i in data:
#     print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2])) 
# print()

data=con.execute("select * from student order by name")
print("{:<15}{:<15}{:<15}".format("age","name","mark"))
print('_'*45)
for i in data:
    print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2])) 
print()