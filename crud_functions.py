import sqlite3


class Products:
    def __init__(self):
        self.path = 'J:\\Python\\DB\\products.db'
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        self.initiate_db()

    def __del__(self):
        self.connection.close()

    def initiate_db(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            price INTEGER,
            image_id INTEGER
            );
        ''')
        for i in range(1, 5):
            self.cursor.execute("INSERT INTO Users (title, description, price, image_id) VALUES(?, ?, ?, ?)",
                                (f"Продукт{i}", f"Описание {i}", f"{i * 100}", f"{i + 10}"))
        self.connection.commit()

    def get_all_products(self):
        self.cursor.execute("SELECT * FROM Users")
        return self.cursor.fetchall()
