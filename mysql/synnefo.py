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
        CREATE TABLE IF NOT EXISTS employe (
            emp_id INT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            email VARCHAR(100),
            position VARCHAR(100),
            salary INT
        )
    ''')

def add_employee(cursor, connection):
    try:
        l = int(input("Enter limit: "))
        for i in range(l):
            emp_id = int(input('Enter employee id: '))
            name = input('Enter your name: ')
            age = int(input('Enter your age: '))
            email = input('Enter your email: ')
            position = input('Enter position: ')
            salary = int(input('Enter your salary: '))
            cursor.execute('INSERT INTO employe (emp_id, name, age, email, position, salary) VALUES (%s, %s, %s, %s, %s, %s)',
                           (emp_id, name, age, email, position, salary))
            connection.commit()
    except Error as e:
        print(f"Error: {e}")

def update_employee(cursor, connection):
    try:
        emp_id = int(input('Enter id of employee to update: '))
        name = input('Enter new name: ')
        age = int(input('Enter new age: '))
        email = input('Enter new email: ')
        position = input('Enter new position: ')
        salary = int(input('Enter new salary: '))
        cursor.execute('UPDATE employe SET name=%s, age=%s, email=%s, position=%s, salary=%s WHERE emp_id=%s',
                       (name, age, email, position, salary, emp_id))
        connection.commit()
    except Error as e:
        print(f"Error: {e}")

def delete_employee(cursor, connection):
    try:
        emp_id = int(input('Enter id of employee to delete: '))
        cursor.execute('DELETE FROM employe WHERE emp_id=%s', (emp_id,))
        connection.commit()
    except Error as e:
        print(f"Error: {e}")

def search_employee(cursor):
    try:
        emp_id = int(input('Enter id to search: '))
        cursor.execute('SELECT * FROM employe WHERE emp_id=%s', (emp_id,))
        data = cursor.fetchall()
        print('{:<10}{:<20}{:<5}{:<30}{:<20}{:<10}'.format('ID', 'Name', 'Age', 'Email', 'Position', 'Salary'))
        print('-' * 75)
        if data:
            for row in data:
                print("{:<10}{:<20}{:<5}{:<30}{:<20}{:<10}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
        else:
            print('ID not available')
    except Error as e:
        print(f"Error: {e}")

def view_all_employees(cursor):
    try:
        cursor.execute('SELECT * FROM employe')
        data = cursor.fetchall()
        print('{:<10}{:<20}{:<5}{:<30}{:<20}{:<10}'.format('ID', 'Name', 'Age', 'Email', 'Position', 'Salary'))
        print('-' * 75)
        for row in data:
            print("{:<10}{:<20}{:<5}{:<30}{:<20}{:<10}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
    except Error as e:
        print(f"Error: {e}")

def group_by(cursor):
    try:
        cursor.execute('SELECT name, MAX(age) AS max_age FROM employe GROUP BY name')
        data = cursor.fetchall()
        print('{:<20}{:<10}'.format('Name', 'Max Age'))
        print('-' * 30)
        if data:
            for row in data:
                print("{:<20}{:<10}".format(row[0], row[1]))
        else:
            print('No data available')
    except Error as e:
        print(f"Error: {e}")

def order_by(cursor):
    try:
        cursor.execute('SELECT * FROM employe ORDER BY age DESC')
        data = cursor.fetchall()
        print('{:<10}{:<20}{:<5}{:<30}{:<20}{:<10}'.format('ID', 'Name', 'Age', 'Email', 'Position', 'Salary'))
        print('-' * 75)
        if data:
            for row in data:
                print("{:<10}{:<20}{:<5}{:<30}{:<20}{:<10}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
        else:
            print('No data available')
    except Error as e:
        print(f"Error: {e}")
     
def like(cursor):
    try:
        pattern = input('Enter pattern to search for in names (e.g., "John"): ')
        cursor.execute('SELECT * FROM employe WHERE name LIKE %s ORDER BY age DESC', (f'%{pattern}%',))
        data = cursor.fetchall()
        print('{:<10}{:<20}{:<5}{:<30}{:<20}{:<10}'.format('ID', 'Name', 'Age', 'Email', 'Position', 'Salary'))
        print('-' * 75)
        if data:
            for row in data:
                print("{:<10}{:<20}{:<5}{:<30}{:<20}{:<10}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
        else:
            print('No matching records found')
    except Error as e:
        print(f"Error: {e}")

     


def main():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        create_table(cursor)

        while True:
            print('\n1. Add\n2. Update\n3. Delete\n4. Search\n5. View All\n6. Group By\n7. Order By\n8. Like\n9.Exit')
            choice = int(input('Enter your choice: '))
            if choice == 1:
                add_employee(cursor, connection)
            elif choice == 2:
                update_employee(cursor, connection)
            elif choice == 3:
                delete_employee(cursor, connection)
            elif choice == 4:
                search_employee(cursor)
            elif choice == 5:
                view_all_employees(cursor)
            elif choice == 6:
                group_by(cursor)
            elif choice == 7:
                order_by(cursor)
            elif choice == 8:
                like(cursor)    
            elif choice == 9:
                break
            else:
                print('Invalid choice...')

        close_connection(connection)


main()
