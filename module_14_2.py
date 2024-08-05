import sqlite3

path = 'J:\\Python\\DB\\not_telegram.db'
connection = sqlite3.connect(path)
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')
cursor.execute("DELETE FROM Users WHERE id = ?",
               (6,))
cursor.execute("SELECT COUNT(*) FROM Users")
count_users = cursor.fetchone()[0]
print(f"Общее количество записей:{count_users}")
cursor.execute("SELECT SUM(balance) FROM Users")
sum_balance = cursor.fetchone()[0]
print(f"Общая сумма балансов:{sum_balance}")
cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance = cursor.fetchone()[0]
print(f"Средний баланс:{avg_balance}")
connection.commit()
connection.close()
