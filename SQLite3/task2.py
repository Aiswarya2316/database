# import sqlite3
# con =sqlite3.connect("sample.db")
# try:
#     con.execute("create table student(age int,name text,mark real)")
# except:
#     pass

# # l=int(input("enter limit:"))
# # for i in range(l):
# #     age=int(input("age"))
# #     name=str(input("name"))
# #     mark=int(input("mark"))

# #     con.execute("insert into student(age,name,mark)values(?,?,?)",(age,name,mark)) 
# #     con.commit()  

# data=con.execute("select * from student")
# print(data)
# print("{;<15}")       
# print()


 # user input

import sqlite3

con = sqlite3.connect("sample.db")#db connection

try:
    con.execute("create table student(age int,name text,mark real)")#create table
except:
    pass

# l= int (input("Enter limit : "))
# for i in range(l):
#     print("------------------------")
#     age =int(input("Enter age : "))
#     name= str(input("Enter name : "))
#     mark = int(input("Enter mark : "))


#     con.execute("insert into student(age,name,mark) values(?,?,?)",(age,name,mark))#add value
#     con.commit()#save




data=con.execute("select * from student ")
print(data)
# for i in data:
#     print(i)





print("{:<15}{:<15}{:<15}".format("age","name","mark"))
print('_'*45)
for i in data:
    print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2])) 
print()