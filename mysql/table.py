import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="aiswaryaa",
            password="aisu123",
            database="mydatabase"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()

def create_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS details (
            emp_id INT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            email VARCHAR(100),
            position VARCHAR(100),
            salary INT
        )
    ''')