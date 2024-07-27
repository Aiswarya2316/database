import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="aiswaryaa",
    password="aisu123"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")