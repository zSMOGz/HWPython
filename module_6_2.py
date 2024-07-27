class Vehicle:
    __COLOR_VARIANTS = ["красный",
                        "синий",
                        "чёрный",
                        "белый"]
    def __init__(self,
                 owner: str,
                 __model: str,
                 __engine_power: int,
                 __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")
        print("")

    def set_color(self,
                  new_color:str):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на: {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Богач', 'Toyota Mark II',  500, 'синий')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('розовый')
vehicle1.set_color('чёрный')
vehicle1.owner = 'Супермеганфокс'

# Проверяем что поменялось
vehicle1.print_info()