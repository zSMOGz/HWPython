import sqlite3

path = 'J:\\Python\\DB\\database.db'
connection = sqlite3.connect(path)
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

cursor.execute('''CREATE INDEX IF NOT EXISTS idx_email ON Users (email)''')
#for i in range(30):
#    cursor.execute("INSERT INTO Users (username, email, age) VALUES(?, ?, ?)",
#                  (f"newuser{i}", f"ex{i}@gmail.com", f"28"))
# for i in range(30):
#     cursor.execute("UPDATE Users SET age = ? WHERE username = ?",
#                    (randint(18, 50), f'newuser{i}'))
# cursor.execute("DELETE FROM Users WHERE username = ?",
#                ('newuser', ))
#cursor.execute("SELECT * FROM Users")
#cursor.execute("SELECT username, age FROM Users WHERE age > ?", (29,))
#cursor.execute("SELECT username, age FROM Users GROUP BY AGE")
# cursor.execute("SELECT COUNT(*) FROM Users")
# total1 = cursor.fetchone()[0]
# total2 = cursor.fetchall()
# cursor.execute("SELECT COUNT(*) FROM Users")
# total2 = cursor.fetchone()[0]
# print(total1/total2) # Для вывода одного элемента используется fetchone
# print(total2) # Т.к.элемент всего один, здесь будет пусто
# cursor.execute("SELECT AVG(*) FROM Users")
# total1 = cursor.fetchone()[0]
# print(total1)
cursor.execute("SELECT MIN(age) FROM Users")
total1 = cursor.fetchone()[0]
print(total1)
cursor.execute("SELECT MAX(age) FROM Users")
total2 = cursor.fetchone()[0]
print(total2)
connection.commit()
connection.close()
