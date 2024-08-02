import random
import time
from threading import Thread
import queue

BURNT_BUN = "Подгоревшая булка"
NORMAL_BUN = "Нормальная булка"


class Bun(Thread):  # Булочка
    def __init__(self,
                 queue):
        self.queue = queue
        super().__init__()

    def run(self):
        while True:
            time.sleep(random.randint(1, 5))
            if random.random() > 0.9:
                self.queue.put(BURNT_BUN)
            else:
                self.queue.put(NORMAL_BUN)


class Cutlet(Thread):  # Котлета
    def __init__(self,
                 queue,
                 count):
        self.queue = queue
        self.count = count
        super().__init__()

    def run(self):
        while self.count:
            # У queue.get есть параметр timeout, который выбрасывает
            # исключение Empty, если не был получен элемент за указанное время
            # Это можно использовать, чтобы не блокировать выполнение ожиданием get
            bun = self.queue.get()
            if bun == NORMAL_BUN:
                time.sleep(random.randint(1, 5))
                self.count -= 1
            print(f"Осталось приготовить булок {self.count}")


# Чтобы процесс, который помещает в очередь не работал слишком быстро
# Можно добоавить ограничение на количество элементов в очереди
queue = queue.Queue(maxsize=10)

t1 = Bun(queue)
t2 = Cutlet(queue, 20)

t1.start()
t2.start()

t1.join()
t2.join()
