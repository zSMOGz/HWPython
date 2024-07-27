class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if (new_floor < 1
                or self.number_of_floors < new_floor):
            print(f'Такого этажа в "{self.name}" не существует')
            return

        print(f'Поднимаемся на этаж {new_floor} в "{self.name}"')
        for floor in range(1, new_floor + 1):
            print(floor)


house1 = House('Дом тысячи кинжалов', 4)
house1.go_to(5)
house1.go_to(-1)
house1.go_to(3)
print('')
house2 = House('ЖК Малыш', 200)
house2.go_to(5)
house2.go_to(-1)
house2.go_to(3)
