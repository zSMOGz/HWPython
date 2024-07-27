class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        House.houses_history.append(args[0])
        print(f'{args[0]} добавлен в историю')
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other

    def __add__(self, other):
        if isinstance(other, House):
            self.number_of_floors += other.number_of_floors
            return self
        elif isinstance(other, int):
            self.number_of_floors += other
            return self

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, House):
            self.number_of_floors -= other.number_of_floors
            return self
        elif isinstance(other, int):
            self.number_of_floors -= other
            return self

    def __rsub__(self, other):
        return self.__sub__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, House):
            self.number_of_floors *= other.number_of_floors
            return self
        elif isinstance(other, int):
            self.number_of_floors *= other
            return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __matmul__(self, other):
        if isinstance(other, House):
            self.number_of_floors *= other.number_of_floors
            return self
        elif isinstance(other, int):
            self.number_of_floors *= other
            return self

    def __rmatmul__(self, other):
        return self.__mul__(other)

    def __imatmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, House):
            self.number_of_floors /= other.number_of_floors
            return self
        elif isinstance(other, int):
            self.number_of_floors /= other
            return self

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __itruediv__(self, other):
        return self.__truediv__(other)

    def __floordiv__(self, other):
        if isinstance(other, House):
            self.number_of_floors //= other.number_of_floors
            return self
        elif isinstance(other, int):
            self.number_of_floors //= other
            return self

    def __rfloordiv__(self, other):
        return self.__floordiv__(other)

    def __ifloordiv__(self, other):
        return self.__floordiv__(other)

    def __pow__(self, other):
        if isinstance(other, House):
            self.number_of_floors **= other.number_of_floors
            return self
        elif isinstance(other, int):
            self.number_of_floors **= other
            return self

    def __rpow__(self, other):
        return self.__pow__(other)

    def __ipow__(self, other):
        return self.__pow__(other)

    def go_to(self, new_floor):
        if (new_floor < 1
                or self.number_of_floors < new_floor):
            print(f'Такого этажа в "{self.name}" не существует')
            return

        print(f'Поднимаемся на этаж {new_floor} в "{self.name}"')
        for floor in range(1, (new_floor + 1)):
            print(floor)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

print('')
print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__

print(House.houses_history)

del h3

print(House.houses_history)