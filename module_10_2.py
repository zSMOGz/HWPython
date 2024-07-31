from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self,
                 name: str,
                 power: int):
        super().__init__()
        self.name = name
        self.power = power

    @staticmethod
    def get_day_str(self,
                    count_day: int):
        if count_day == 1:
            return 'день'
        elif 1 < count_day < 5:
            return 'дня'
        else:
            return 'дней'

    def run(self):
        print(f'{self.name}, на нас напали!')

        current_day = 0
        count_enemy = 100
        for enemies in range(self.power, count_enemy + self.power, self.power):
            current_day += 1

            print(f'{self.name} сражается {current_day} {Knight.get_day_str(self, current_day)}'
                  + f'..., осталось {count_enemy - enemies} врагов')

            sleep(1)

        print(f'{self.name} одержал победу спустя {current_day} {Knight.get_day_str(self, current_day)}!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

threads = []

first_knight.start()
second_knight.start()
threads.append(first_knight)
threads.append(second_knight)

for thread in threads:
    thread.join()
