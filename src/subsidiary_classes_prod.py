from src.creating_classes import Product


class Smartphone(Product):
    """Создание класса - Смартфон"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Конструктор экземпляра класса Smartphone"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Создание класса - Трава газонная"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Конструктор экземпляра класса Smartphone"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
