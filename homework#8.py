import sqlite3


connect = sqlite3.connect("users.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30) NOT NULL,
        age INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades(
        grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject VARCAHR(100) NOT NULL,
        grade INTEGER NOT NULL,
        userid INTEGER,
        FOREIGN KEY (userid) REFERENCES users(user_id)
    )
''')
connect.commit()



cursor.execute('''
    CREATE VIEW IF NOT EXISTS my_view AS
        SELECT users.name, users.age, grades.subject, grades.grade FROM users
        LEFT JOIN grades ON users.user_id = grades.userid
        WHERE user.age >= 18 AND user.age >= 70;
        WHERE grades.grade IS NOT NULL;

''')


def add_user(name: str, age: int):

    cursor.execute(
        'INSERT INTO users(name, age) VALUES (?,?)',
        (name, age)
    )
    connect.commit()
    print(f"{name} - Добавили")

# add_user("user", 14)
# add_user("user2", 19)
# add_user("user3", 22)
# add_user("user4", 33)

def add_grade(user_id, subject, grade):
    cursor.execute(
        'INSERT INTO grades(userid, subject, grade) VALUES (?,?,?)',
        (user_id, subject, grade)
    )
    connect.commit()

    print("Оценка за урок добавлена!!")


# add_grade(4, "Алгебра", 5)
# add_grade(99, "Физика", 5)


def get_user_and_grade():

    cursor.execute('''
        SELECT users.name, grades.subject, grades.grade
        FROM users FULL OUTER JOIN grades ON users.user_id = grades.userid
    ''')

    users = cursor.fetchall()

    for i in users:
        print(f"name: {i[0]}, subject: {i[1]}, grade: {i[2]}")


def get_max_age():
    cursor.execute('SELECT AVG(age) FROM users')

    print(cursor.fetchone())

def create_view_test():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS view_test AS
        SELECT name, age, subject, grade
        FROM users LEFT JOIN grades ON users.user_id = grades.userid
        WHERE age = 19
    ''')
    print('Пердставление создано!!')



def get_user_age_19():
    cursor.execute('SELECT * FROM view_test')

    print(cursor.fetchone())

get_user_age_19()