import sqlite3
con=sqlite3.connect("employe.db")
try:
        con.execute("create table (name text,place text,c_no int,address text)")
except:
        pass
# con.execute("insert into dtls(name,place,c_no,address)values('alan','vkm',1453652,'vkm')")
# con.commit()
# con.execute("insert into dtls(name,place,c_no,address)values('mwonu','ekm',1453652,'ekm')")
# con.commit()

# data=con.execute("select marks.name,marks.age,marks.mark,dtls.place,dtls.c_no,dtls.address from marks inner join dtls on marks.name=dtls.name")
# for i in data:
#         print(i)