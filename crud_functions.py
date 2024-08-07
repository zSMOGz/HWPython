import sqlite3


class DB:
    def __init__(self):
        self.path = 'J:\\Python\\DB\\products.db'
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        self.initiate_db()

    def __del__(self):
        self.connection.close()

    def initiate_db(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            price INTEGER,
            image_id INTEGER
            );
        ''')
        self.connection.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY,
            user_name TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER,
            balance INTEGER
            );
        ''')
        self.connection.commit()

        # for i in range(1, 5):
        #     self.cursor.execute("INSERT INTO Products (title, description, price, image_id) VALUES(?, ?, ?, ?)",
        #                         (f"Продукт{i}", f"Описание {i}", f"{i * 100}", f"{i + 10}"))
        self.connection.commit()

    def get_all_products(self):
        self.cursor.execute("SELECT * FROM Products")
        return self.cursor.fetchall()

    def add_user(self,
                 user_name,
                 email,
                 age):
        user_included = self.is_included(user_name)
        if user_included is False:
            self.cursor.execute(f'''INSERT INTO Users (user_name, email, age, balance) VALUES( 
                                '{user_name}', 
                                '{email}', 
                                '{age}',
                                0)
            ''')
            self.connection.commit()
        self.connection.close()

    def is_included(self,
                    user_name):
        user = self.cursor.execute(f"SELECT id FROM Users WHERE user_name = '{user_name}'").fetchone()
        self.connection.commit()
        if user is not None:
            return True
        else:
            return False
