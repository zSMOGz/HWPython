import sqlite3

path = 'J:\\Python\\DB\\database.db'
connection = sqlite3.connect(path)
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
user_name TEXT NOT NULL,
first_name TEXT NOT NULL,
block INTEGER
);
''')


def add_user(user_id,
             user_name,
             first_name):
    check_user = cursor.execute("SELECT * FROM Users WHERE id=?",
                                (user_id,))
    if check_user.fetchone() is None:
        cursor.execute(f'''INSERT INTO Users VALUES('{user_id}', 
                       '{user_name}', '{first_name}', 0)
        ''')
        connection.commit()
    connection.close()


def show_users():
    users_list = cursor.execute("SELECT * FROM USERS")
    message = ""
    for user in users_list:
        message += f"{user[0]} @{user[1]} {user[2]}\n"
    connection.commit()
    return message


def show_stat():
    count_users = cursor.execute("SELECT COUNT(*) FROM Users").fetchone()
    connection.commit()
    return count_users[0]


def add_to_block(user_id):
    cursor.execute(f"UPDATE Users SET block = ? WHERE id = ?",
                   (1, user_id))
    connection.commit()


def remove_from_block(user_id):
    cursor.execute(f"UPDATE Users SET block = ? WHERE id = ?",
                   (0, user_id))
    connection.commit()


def check_block(user_id):
    block_user = cursor.execute(f"SELECT block FROM Users WHERE id = {user_id}").fetchone()
    connection.commit()
    return block_user[0]
