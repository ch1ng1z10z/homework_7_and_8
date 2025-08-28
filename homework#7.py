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


def sozdanie_user(name_1, age_1, hobby_1):
    cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES("{name_1}", "{age_1}", "{hobby_1}")')
    connect.commit()
    print('Пользователь добавлен!!')
sozdanie_user('Анна', 23, "красить")
sozdanie_user('Николай', 58, "спать")
sozdanie_user('венник', 2, "убирать")
sozdanie_user('Уролог', 34, "смотреть")
sozdanie_user('Венерена', 400000, "перемещяться")

def get_users():
    cursor.execute('SELECT name, age, hobby FROM users')
    users = cursor.fetchall()

    for i in users:
        print(f"ИМЯ: {i[0]}, ВОЗРАСТ: {i[1]}, ХОББИ: {i[2]}")



def update_user(name, row_id):
    cursor.execute(f'UPDATE users SET name = "{name}" WHERE rowid = "{row_id}"')
    connect.commit()
    print('Пользователь обновлён')

update_user("Macho_men", 14)


def delete_user(row_id):

    cursor.execute(f'DELETE FROM users WHERE id = "{row_id}"')
    connect.commit()
    print('Пользователь удален!')

delete_user(4)

get_users()

def get_user_by_id(user_id):
    if cursor.execute(f'SELECT name, age, hobby FROM users WHERE id = {user_id}'):
        return print(get_user_by_id(2))
    else:
        return print(f'Пользователь не найден')

