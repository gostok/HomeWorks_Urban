import sqlite3
import random

def initial_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')
    connection.commit()
    connection.close()

# initial_db()


def create_products():
    for i in range(1, 5):
        connection = sqlite3.connect('products.db')
        cursor = connection.cursor()

        cursor.execute("INSERT INTO Products(title, description, price) VALUES (?, ?, ?)",
                       (f'Продукт {i}', f'Описание {i}', f'{i}00'))

        connection.commit()
        connection.close()

# create_products()


def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT title, description, price FROM Products')
    res = cursor.fetchall()

    products = []
    for i in res:
        product = {
            'title': i[0],
            'description': i[1],
            'price': i[2]
        }
        products.append(product)

    connection.commit()
    connection.close()

    return products

# get_all_products()
