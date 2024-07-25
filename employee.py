import sqlite3

con = sqlite3.connect("task3.db")#db connection

try:
            con.execute("create table employee(name text,age int,email text,sal int,pos text,exp int)")#create table
except:
            pass


while True:
    ch=int(input("1.Add \n2.Update \n3.Delete \n4.Display \n5.Search \n6.Exit\nEnter choice :"))
    if ch ==1:
        l= int (input("Enter limit : "))
        for i in range(l):
            print('_'*80)
            name= str(input("Enter name : "))
            age =int(input("Enter age : "))
            email = str(input("Enter email : "))
            sal=int(input("Enter salary : "))
            pos=str(input("Enter position : "))
            exp=int(input("Enter experiance : "))


            con.execute("insert into employee(name,age,email,sal,pos,exp) values(?,?,?,?,?,?)",(name,age,email,sal,pos,exp))#add value
            con.commit()#save




        data=con.execute("select * from employee ")
        print(data)
        # for i in data: ##print all
        #     print(i)





        print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format("name","age","email","salary","position","experiance")) ##print in a table
        print('_'*80)
        for i in data:
            print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5])) 
        print()
        





                ##update name ,user input

    elif ch==2:
        # try:
        #     con.execute("create table employee(age int,name text,email real)")#create table
        # except:
        #     pass


        name=str(input("Enter old name : "))
        new=str(input("Enter new name : "))
        con.execute("update employee set name=? where name =?",(new,name))
        con.commit()
        data=con.execute("select * from employee")

        print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format("name","age","email","salary","position","experiance")) ##print in a table
        print('_'*80)
        for i in data:
            print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5])) 
        print()
        


    elif ch ==3:



        name=str(input("Enter name : "))
        con.execute("delete from employee where name =?",(name,))
        con.commit()
        data=con.execute("select * from employee")

        print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format("name","age","email","salary","position","experiance")) ##print in a table
        print('_'*80)
        for i in data:
            print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5])) 
        print()
        

    
    elif ch ==4:

        data=con.execute("select * from employee")

        print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format("name","age","email","salary","position","experiance")) ##print in a table
        print('_'*50)
        for i in data:
            print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5])) 
        print()
        

    elif ch ==5:


        name=str(input("Enter name : "))

        data=con.execute("select * from employee where name=? ",(name,))

        print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format("name","age","email","salary","position","experiance")) ##print in a table
        print('_'*80)
        for i in data:
            print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5])) 
        print()
        

    elif ch ==6:
        print("You had exited")
        break    