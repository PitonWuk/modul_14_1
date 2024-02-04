"""
Завдання 3
Додайте до першого завдання можливість збереження
результатів фільтрів у файл. Шлях і назву файлу вкажіть у
налаштуваннях програми.
"""
import sqlite3

SAVE_RESULTS_TO_FILE = True
RESULTS_FILE_PATH = "results.txt"

def initialize_database():
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Sales (
            id INTEGER PRIMARY KEY,
            salesman_id INTEGER,
            customer_id INTEGER,
            amount REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Salesmen (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    ''')

    conn.commit()
    conn.close()

def insert_data(table_name, data):
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()
    query = f"INSERT INTO {table_name} VALUES ({','.join(['?'] * len(data))})"
    cursor.execute(query, data)
    conn.commit()
    conn.close()

def update_data(table_name, set_values, condition):
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()
    query = f"UPDATE {table_name} SET {','.join([f'{column}=?' for column in set_values])} WHERE {condition}"
    cursor.execute(query, set_values.values())
    conn.commit()
    conn.close()

def delete_data(table_name, condition):
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()
    query = f"DELETE FROM {table_name} WHERE {condition}"
    cursor.execute(query)
    conn.commit()
    conn.close()

def display_all_data(table_name):
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()
    for row in data:
        print(row)
    conn.close()


    if SAVE_RESULTS_TO_FILE:
        with open(RESULTS_FILE_PATH, 'w') as file:
            for row in data:
                file.write(str(row) + '\n')

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Insert Data")
        print("2. Update Data")
        print("3. Delete Data")
        print("4. Display All Data")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            table_name = input("Enter table name (Sales, Salesmen, Customers): ")
            data = input("Enter data separated by commas: ").split(',')
            insert_data(table_name, data)
        elif choice == '2':
            table_name = input("Enter table name (Sales, Salesmen, Customers): ")
            set_values = input("Enter set values (column1=value1,column2=value2,...): ").split(',')
            condition = input("Enter condition (column1=value1): ")
            update_data(table_name, dict([value.split('=') for value in set_values]), condition)
        elif choice == '3':
            table_name = input("Enter table name (Sales, Salesmen, Customers): ")
            condition = input("Enter condition (column1=value1): ")
            delete_data(table_name, condition)
        elif choice == '4':
            table_name = input("Enter table name (Sales, Salesmen, Customers): ")
            display_all_data(table_name)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

initialize_database()
main_menu()
