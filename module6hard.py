import math


class Figure:
    sides_count = 0

    def __init__(self,
                 colors: list[int],
                 filled: bool = True,
                 *_sides):
        self.__sides = None
        self.set_sides(*_sides)
        self.__colors = list(colors)
        self.filled = filled

    def get_color(self):
        return self.__colors

    def __is_valid_color(self,
                         r: int,
                         g: int,
                         b: int):
        if (r in range(1, 256)
                and g in range(1, 256)
                and b in range(1, 256)):
            return True
        else:
            return False

    def set_color(self,
                  r: int,
                  g: int,
                  b: int):
        if self.__is_valid_color(r, g, b):
            self.__colors.clear()
            self.__colors.append(r)
            self.__colors.append(g)
            self.__colors.append(b)

    def __is_valid_sides(self,
                         *sides):
        # Если хотя бы один элемент не целое число
        for side in sides:
            if not isinstance(side, int):
                return False
        # Если количество элементов не совпадает с текущим
        if len(sides) != self.sides_count:
            return False
        # Если сторона - не положительное число
        for side in sides:
            if side <= 0:
                return False

        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        length: int = 0
        for side in self.__sides:
            length += side

        return length

    def set_sides(self,
                  *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_square(self):
        return 0


class Circle(Figure):
    sides_count = 1

    def __init__(self,
                 colors: list[int],
                 radius: int = 1,
                 filled: bool = True):
        self.__radius = radius
        __sides = self.__radius
        super().__init__(colors,
                         filled,
                         __sides)

    def get_square(self):
        return math.pi * (self.__radius * self.__radius)


class Triangle(Figure):
    sides_count = 3

    def __init__(self,
                 colors: list[int],
                 filled: bool = True,
                 *__sides):
        super().__init__(colors,
                         filled,
                         __sides)
        __sides = self.get_sides()
        # Полупериметр
        p = sum(__sides) / 2

        __height = (2 / __sides[0] * self.get_square())

    def get_half_meter(self):
        return sum(self.get_sides()) / 2

    def get_square(self):
        p = self.get_half_meter()
        current_sides = self.get_sides()
        return math.sqrt(p * (p - current_sides[0]) * (p - current_sides[1]) * (p - current_sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self,
                 colors: list[int],
                 side_length: int,
                 filled: bool = True):
        __sides = []
        for side in range(0, self.sides_count):
            __sides.append(side_length)
        super().__init__(colors,
                         filled,
                         *__sides)

    def get_volume(self):
        _sides = self.get_sides()
        return _sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
sides = cube1.get_sides()
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
