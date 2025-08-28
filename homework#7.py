import sqlite3


# A4
connect = sqlite3.connect("users.db")
# Рука с ручкой
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (100) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()

# CRUD - Create Read Update Delete

def add_user(name_1, age_1, hobby_1):
    # cursor.execute(
    #     "INSERT INTO users(name, age, hobby) VALUES(?, ?, ?)",
    #     (name_1, age_1, hobby_1)
    # )
    cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES("{name_1}", "{age_1}", "{hobby_1}")')
    connect.commit()
    print('Пользователь добавлен!!')
add_user('Андрей', 15, "Летать")