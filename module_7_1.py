class Product:
    def __init__(self,
                 name: str,
                 weight: float,
                 category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

    def __repr__(self):
        return f'[{self.name}, {self.weight}, {self.category}]'

    def __eq__(self, other):
        if self.name == other:
            return True
        else:
            return False


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        products = []

        try:
            file = open(self.__file_name, 'r')
        except:
            return []
        lines = [line.rstrip() for line in file]
        for line in lines:
            split_line = line.split(', ')
            products.append(Product(split_line[0],
                                    float(split_line[1]),
                                    split_line[2]))
        file.close()

        return products

    def add(self,
            *products: Product):
        current_products = self.get_products()

        file = open(self.__file_name, 'a')
        for product in products:
            if product not in current_products:
                file.write(f'{product}\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
