import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="aiswaryaa",
    password="aisu123",
    database="mydatabase"
)

cursor = mydb.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS DETAILS(name TEXT,emp_id INT PRIMARY KEY, address TEXT)")


cursor.execute("select employe.emp_id,employe.name,employe.age,employe.email,employe.position,employe.salary,DETAILS.name,DETAILS.address,DETAILS.emp_id from employe right join DETAILS on employe.emp_id=DETAILS.emp_id")
data=cursor.fetchall()
for i in data:
    print(i)
print()    
# while True:
#     print("1.Add\n2.Update\n3.Delete\n4.Search\5.View all\n6.Exit")
#     ch=int(input("enter ur choice:"))
#     if ch==1:
#         # l=int(input("enter the limit:"))
#         name=str(input("enter name:"))
#         emp_id=int(input("enter id:"))
#         address=str(input("enter address:"))
#         cursor.execute('INSERT INTO DETAILS (emp_id, name, address) VALUES (%s, %s, %s)',(emp_id, name, address))
#         mydb.commit()
