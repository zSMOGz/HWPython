import queue
import threading
import time


class Table:
    def __init__(self,
                 number: int):
        self.number = number
        self.is_busy = False


class Customer:
    __customers_count = 0

    def __init__(self,
                 _cafe):
        Customer.__customers_count += 1
        self.number = Customer.__customers_count
        self._cafe = _cafe

    def customer_take_table(self,
                            table,
                            q: queue):
        print(f'Посетитель №{self.number} сел за стол {table.number}')
        table.is_busy = True
        time.sleep(5)
        table.is_busy = False
        print(f'Посетитель №{self.number} покушал и ушёл')

        customer = q.get()
        if customer is not None:
            serve_thread = threading.Thread(target=customer._cafe.serve_customer, args=(customer,))
            serve_thread.start()


class Cafe:
    def __init__(self,
                 tables: list[Table]):
        self.queue_in_cafe = queue.Queue()
        self.tables = tables
        self.__max_count_customer_per_day = 0
        self.__current_count_customer_per_day = 0

    def customer_arrival(self,
                         max_count_customer):
        self.__max_count_customer_per_day = max_count_customer

        while True:
            if self.__current_count_customer_per_day < self.__max_count_customer_per_day:
                time.sleep(1)

                customer = Customer(self)

                self.__current_count_customer_per_day += 1
                print(f'Посетитель №{customer.number} прибыл')

                serve_thread = threading.Thread(target=self.serve_customer, args=(customer,))
                serve_thread.start()

    def serve_customer(self,
                       customer):
        table = cafe.get_table_available()

        if table is not None:
            customer_thread = threading.Thread(target=customer.customer_take_table,
                                               args=(table, self.queue_in_cafe, ))
            customer_thread.start()
        else:
            self.queue_in_cafe.put(customer)
            print(f'Посетитель №{customer.number} ожидает свободный стол')

    def get_table_available(self):
        for table in self.tables:
            if not table.is_busy:
                return table
        return None


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival, args=(20,))
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
