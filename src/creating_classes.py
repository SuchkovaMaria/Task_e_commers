from typing import List


class Product:
    """Создание класса - Товар"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Конструктор экземпляра класса Product"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """Метод вывода данных продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод сложения цен двух продуктов (каждая цена умножена на количество шт. на складе)"""
        if (
            type(other) is self.__class__
        ):  # сложение только экземпляров одного класса (поэтому сравнение с классом первого экземпляра)
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError("Сложение не корректных типов данных")

    @property
    def price(self):
        """Вывод цены продукта"""
        return self.__price

    @price.setter
    def price(self, price):
        """Изменение цены продукта"""
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price

    @classmethod
    def new_product(cls, product):
        """Метод для создания продукта"""
        return cls(product["name"], product["description"], product["price"], product["quantity"])


class Category:
    """Создание класса - Категория (для товаров)"""

    name: str
    description: str
    __products: List[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Конструктор экземпляра класса Category"""
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count = len(self.__products)

    def __str__(self):
        """Вывод информации по категории"""
        product_count = []
        for product in self.__products:
            product_count.append(product.quantity)
        return f"{self.name}, количество продуктов: {sum(product_count)} шт."

    @property
    def products(self):
        """Вывод списка пропуктов в категории (строкой)"""
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @property
    def products_in_list(self):
        """Вывод списка продуктов в категории (list)"""
        return self.__products

    def add_product(self, product):
        """Класс-метод для добавления товара в список продуктов"""

        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Введенные данные являются продутком")
