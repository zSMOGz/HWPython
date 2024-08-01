from multiprocessing import Process, Manager


class WarehouseManager(Process):
    def __init__(self):
        super().__init__()
        self.data = {}

    def process_request(self,
                        request: tuple):
        if request[1] == 'receipt':
            if request[0] in self.data:
                self.data[request[0]] += int(request[2])
            else:
                self.data[request[0]] = int(request[2])
        elif request[1] == 'shipment':
            if request[0] in self.data:
                if self.data[request[0]] >= int(request[2]):
                    self.data[request[0]] -= int(request[2])
                else:
                    print(f'Товара: {request[0]} недостаточно для отгрузки.'
                          f' Текущее количество: {self.data[request[0]]}')
            else:
                print(f'Товара: {request[0]} нет в наличии')

    def run(self,
            requests):
        if __name__ == '__main__':
            process_manager = Manager()
            self.data = process_manager.dict()
            for request in requests:
                p = Process(target=manager.process_request, args=(request,))
                p.start()
                p.join()


# Создаем менеджера склада
manager = WarehouseManager()

# Множество запросов на изменение данных о складских запасах
requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]

# Запускаем обработку запросов
manager.run(requests)

# Выводим обновленные данные о складских запасах
if len(manager.data) > 0:
    print(manager.data)
