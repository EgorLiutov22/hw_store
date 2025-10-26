class EmptyStockException(Exception):
    pass


class Product:
    '''
    Атрибуты:
    -name (строка) — название товара;
    -price (число) — цена товара;
    -stock (целое число) — количество товара на складе.
    Методы:
    -update_stock(quantity) — метод, который обновляет количество товара на складе. Если количество становится отрицательным, должно выдаваться сообщение об ошибке.
    '''
    def __init__(self, name, price, stock):
        self.price = price
        self.name = name
        self.stock = stock

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = float(price)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = str(name)

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):
        stock = int(stock)
        if stock >= 0:
            self.__stock = stock
        else:
            raise EmptyStockException('stock cannot be lover than 0')

    def __isub__(self, quantity):
        self.stock -= quantity
        return self

    def __str__(self):
        return self.__name

    def __hash__(self):
        return hash((self.name, self.price))

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.stock})"

    def update_stock(self, quantity):
        self.stock = quantity
