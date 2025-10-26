from order import Order


class Store:
    '''
    Атрибуты:
    -products (список) — список всех доступных товаров в магазине.
    Методы:
    -add_product(product) — метод для добавления товара в магазин;
    -list_products() — метод для отображения всех товаров в магазине с их ценами и количеством на складе;
    -create_order() — метод для создания нового заказа.

    '''

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def list_products(self):
        for i, product in enumerate(self.__products):
            print(f'{i+1}. {product.name} цена:{product.price}, количество:{product.stock}')

    @staticmethod
    def create_order():
        return Order()
