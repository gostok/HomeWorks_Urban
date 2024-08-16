import sqlite3
import random


def initial_db():
    with sqlite3.connect('products.db') as connection:
        cursor = connection.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INT NOT NULL
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INT NOT NULL,
        balance INT NOT NULL
        )
        ''')
        connection.commit()


# initial_db()

def create_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    for i in range(1, 5):
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

def add_user(username, email, age):
    with sqlite3.connect('products.db', timeout=10) as connection:
        cursor = connection.cursor()
        check_user = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
        if check_user.fetchone() is None:
            cursor.execute('''
            INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)
            ''', (username, email, age, 1000))
        connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    query = cursor.execute("SELECT COUNT(*) FROM Users WHERE username = ?", (username,))
    result = cursor.fetchone()[0]
    connection.commit()

    return result > 0

