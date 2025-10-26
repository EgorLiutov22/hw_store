class Order:
    '''
    Атрибуты:
    -products (словарь) — словарь, где ключом является объект Product, а значением — количество этого товара в заказе.
    Методы:
    -add_product(product, quantity) — метод для добавления товара в заказ. Если товара недостаточно на складе, должно выдаваться сообщение об ошибке;
    -calculate_total() — метод для расчёта общей стоимости заказа.

    '''
    def __init__(self):
        self.__products = {}

    @property
    def products(self):
        return self.__products

    def add_product(self, product, quantity):
        try:
            product -= quantity
            self.__products[product] = quantity
        except Exception as e:
            print(e)

    def calculate_total(self):
        return sum(map(lambda x: x.price * self.__products[x], self.__products))
