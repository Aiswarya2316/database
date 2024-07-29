import sqlite3

con = sqlite3.connect("employees.db")

try:
    con.execute("create table employee(name text,age int,email text,sal int,pos text,exp int)")#create table
except:
    pass


while True:
    # ch=int(input("1.Add \n2.Update \n3.Delete \n4.Display \n5.Search \n6.Exit\nEnter choice :"))
    # if ch ==1:
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
            con.commit()

        data=con.execute("select * from employee ")
        print(data)

        print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format("name","age","email","salary","position","experiance")) ##print in a table
        print('_'*80)
        for i in data:
            print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5])) 
        print()
        

    # elif ch==2:  
    #     name=str(input("Enter old name : "))
    #     data=con.execute("select * from employee where name=? ",(name,))
    #     found=False
    #     for i in data:
    #         found=True
    #         new=str(input("Enter new name : "))
    #         con.execute("update employee set name=? where name =?",(new,name))
    #         con.commit()
    #         data=con.execute("select * from employee")
    #         print("Updated succesfully !")
            
    #     if not found:
    #         print("Invalid Input !")


    # elif ch ==3:

    #     name=str(input("Enter name : "))
    #     data=con.execute("select * from employee where name=? ",(name,))
    #     found=False
    #     for i in data:
    #         found=True
    #         con.execute("delete from employee where name =?",(name,))
    #         con.commit()
    #         data=con.execute("select * from employee")
    #         print("Deleted duccessfully !")

    #     if not found:
    #         print("Invalid Input !")
 
    # elif ch ==4:

    #     data=con.execute("select * from employee")

    #     print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format("name","age","email","salary","position","experiance")) ##print in a table
    #     print('_'*80)
    #     for i in data:
    #         print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5])) 
    #     print()
        

    # elif ch ==5:
    #     sname=str(input("Enter name : "))
    #     data=con.execute("select * from employee where name=? ",(sname,))  
    #     found = False
    #     for i in data:

    #         print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format("name","age","email","salary","position","experiance")) ##print in a table
    #         print('_'*80)
    #         print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5])) 
    #         print()
    #         found=True
    #     if not found:
    #         print("Invalid Input !")
        

    # elif ch ==6:
    #     print("You had exited")
    #     break    

    # else:
    #      ("invalid input")