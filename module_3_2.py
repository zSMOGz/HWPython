default_mail = "university.help@gmail.com"


def validate_email(mail: str):
    if (mail.find('@') == -1
            or (mail[-4:] != '.com'
                and mail[-4:] != '.net'
                and mail[-3:] != '.ru')):
        return False
    else:
        return True


def send_email(message: str, recipient: str, *, sender=default_mail):
    if (validate_email(sender) is False
            or validate_email(recipient) is False):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if recipient == sender:
        print(f"Нельзя отправлять письма самому себе")
        return

    if sender == default_mail:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
        return
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
        return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
