import sqlite3
con =sqlite3.connect("employeee.db")
try:
    con.execute("create table staf(name text,age int, id int,JobTitle text,Department text,Email text,Location text,StartDate int,sallary real)")
except:
    pass
while True:
    choice=int(input("1.insert\n2.update\n3.delete\n4.view\n5.search\n6.exit\nenter ur choice:"))
    if choice==1:
        l=int(input("enter limit:"))
        for i in range(l):
            print("------------------")
            name=str(input("enter ur name:"))
            age=int(input("Enter ur age:"))
            id=int(input("enter ur id:"))
            JobTitle=str(input("enter title:"))
            Department=str(input("enter ur departmaent:"))
            Email=str(input("enter ur mail:"))
            Location=str(input("enter ur location:"))
            StartDate=int(input("enter ur joining date:"))
            sallary=int(input("enter ur sallary:"))
            con.execute("insert into staf(name,age,id,JobTitle,Department,Email,Location,StartDate,sallary)",(name,age,id,JobTitle,Department,Email,Location,StartDate,sallary))
            con.commit
        data=con.execute("select * from student")
        print(data)
        print("{:<15}{:<15}{:<15}".format("name","age","id","JobTitle","Department","Email","location","StartDate","sallary"))
        print('_'*45)
        for i in data:
            print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2])) 
        print()    