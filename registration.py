class Database:
    """
    Класс для работы с данными
    """

    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

    @staticmethod
    def verify_password(password: str):
        if (len(password) < 8
                or not any(map(str.isdigit, password))):
            return False
        else:
            return True


if __name__ == '__main__':
    database = Database()

    while True:
        choise = input("Привет! Выбери действие:"
                       + "\n1 - Вход"
                       + "\n2 - Регистрация\n")
        match choise:
            case '1':
                login = input('Введите логин: ')
                password = input('Введите пароль: ')

                if login in database.data:
                    if password == database.data[login]:
                        print('Вход выполнен')
                    else:
                        print('Неверный пароль')
                else:
                    print('Такого пользователя нет')
            case '2':
                user = User(input('Введите логин: '),
                            password := input('Введите пароль: '),
                            password_confirm := input('Повторите пароль: '))

                if not User.verify_password(password):
                    print('Пароль должен содержать цифру и быть больше 8 символов')
                    continue

                if password != password_confirm:
                    print('Пароли не совпадают')
                    continue

                database.add_user(user.username, user.password)

    print(database.data)
