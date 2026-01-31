from typing import List


class Product:
    """Создание класса - Товар"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price

    @classmethod
    def new_product(cls, propuct):
        for k, v in propuct.items():
            if k == "name":
                name = v
            elif k == "description":
                description = v
            elif k == "price":
                price = v
            elif k == "quantity":
                quantity = v
        return cls(name, description, price, quantity)


class Category:
    """Создание класса - Категория (для товаров)"""

    name: str
    description: str
    __products: List[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count = len(self.__products)

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @property
    def products_in_list(self):
        return self.__products

    def add_product(self, product: Product):
        """Класс-метод для добавления товара в список продуктов"""

        self.__products.append(product)
        Category.product_count += 1
