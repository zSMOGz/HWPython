from threading import Thread, Lock


class BankAccount:
    def __init__(self,
                 account,
                 amount):
        self.account = account
        self.amount = amount

    def deposit(self,
                amount):
        self.amount += amount
        print(f'Счёт пополнен на {amount}, на счету {self.amount}')

    def withdraw(self,
                 amount):
        self.amount -= amount
        print(f'Со счёта сняты {amount}, на счету {self.amount}')


lock = Lock()


def deposit_task(bank_account,
                 amount):
    for _ in range(5):
        with lock:
            bank_account.deposit(amount)


def withdraw_task(bank_account,
                  amount):
    for _ in range(5):
        with lock:
            bank_account.withdraw(amount)


current_account = BankAccount(134234235,
                      1000)

deposit_thread = Thread(target=deposit_task, args=(current_account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(current_account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
