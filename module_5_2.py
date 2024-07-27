class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} удалён')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def go_to(self, new_floor):
        if (new_floor < 1
                or self.number_of_floors < new_floor):
            print(f'Такого этажа в "{self.name}" не существует')
            return

        print(f'Поднимаемся на этаж {new_floor} в "{self.name}"')
        for floor in range(1, (new_floor + 1)):
            print(floor)


house1 = House('Дом тысячи кинжалов', 4)
house1.go_to(5)
house1.go_to(-1)
house1.go_to(3)
print(f'Всего этажей: {len(house1)}')
print(str(house1))
print('')
house2 = House('ЖК Малыш', 200)
house2.go_to(5)
house2.go_to(-1)
house2.go_to(3)
print(f'Всего этажей: {len(house2)}')
print(str(house2))
