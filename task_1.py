"""
Завдання 1
Створіть тритабличну базу даних Sales (Продажі). У цій
базі даних мають бути таблиці: Sales (інформація про конкретні
продажі), Salesmen (інформація про продавців), Customers (інформація про покупців). Створіть додаток для відображення
даних з таблиць. Меню додатку має містити такий мінімальний набір звітів:
■ Відображення усіх угод;
■ Відображення угод конкретного продавця;
■ Відображення максимальної за сумою угоди;
■ Відображення мінімальної за сумою угоди;
■ Відображення максимальної суми угоди для конкретного
продавця;
■ Відображення мінімальної за сумою угоди для конкретного продавця;
■ Відображення максимальної за сумою угоди для конкретного покупця;
■ Відображення мінімальної за сумою угоди для конкретного покупця;
■ Відображення продавця з максимальною сумою продажів
за всіма угодами;
■ Відображення продавця з мінімальною сумою продажів
за всіма угодами;
■ Відображення покупця з максимальною сумою покупок
за всіма угодами;
■ Відображення середньої суми покупки для конкретного
покупця;
■ Відображення середньої суми покупки для конкретного
продавця
"""

import sqlite3

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


cursor.execute("INSERT INTO Salesmen (name) VALUES ('John')")
cursor.execute("INSERT INTO Salesmen (name) VALUES ('Alice')")

cursor.execute("INSERT INTO Customers (name) VALUES ('Bob')")
cursor.execute("INSERT INTO Customers (name) VALUES ('Emma')")

cursor.execute("INSERT INTO Sales (salesman_id, customer_id, amount) VALUES (1, 1, 100.0)")
cursor.execute("INSERT INTO Sales (salesman_id, customer_id, amount) VALUES (2, 2, 150.0)")

conn.commit()


def display_all_sales():
    cursor.execute("SELECT * FROM Sales")
    sales = cursor.fetchall()
    print("All Sales:")
    for sale in sales:
        print(sale)

def display_sales_by_salesman(salesman_id):
    cursor.execute("SELECT * FROM Sales WHERE salesman_id=?", (salesman_id,))
    sales = cursor.fetchall()
    print(f"Sales by Salesman {salesman_id}:")
    for sale in sales:
        print(sale)

def display_max_sale():
    cursor.execute("SELECT MAX(amount) FROM Sales")
    max_sale = cursor.fetchone()[0]
    print(f"Max Sale Amount: {max_sale}")

def display_min_sale():
    cursor.execute("SELECT MIN(amount) FROM Sales")
    min_sale = cursor.fetchone()[0]
    print(f"Min Sale Amount: {min_sale}")


display_all_sales()
display_sales_by_salesman(1)
display_max_sale()
display_min_sale()


conn.close()
