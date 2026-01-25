import pytest

from src.base_classes import BaseProduct


def test_base_classes_1():
    """Проверка что класс имеет функционал абстрактного"""

    class Test(BaseProduct):
        """Класс для теста"""

        def __init__(self, name, price):
            self.name = name
            self.price = price

        def __repr__(self):
            return f"<Test: {self.name}, price: {self.price}>"

        @classmethod
        def new_product(cls, dict_test):
            return cls(dict_test["name"], dict_test["price"])

    test1 = Test.new_product({"name": "appel", "price": 100})
    assert test1.name == "appel"


def test_base_classes_2(capsys):
    """Проверка что класс не имеет функционал абстрактного"""

    class Test(BaseProduct):
        """Класс для теста"""

        def __init__(self, name, price):
            self.name = name
            self.price = price

    with pytest.raises(TypeError):
        Test("appel", 100)
