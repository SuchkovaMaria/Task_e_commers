from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный клас определяющий общие методы для класса Продукты"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """Метод создания экземпляра класса Продукт"""
        pass
