import pytest

from src.creating_classes import Category, Product
from src.subsidiary_classes_prod import LawnGrass, Smartphone


@pytest.fixture
def product_1():
    return Product("Рис", "Крупа", 75.5, 10)


@pytest.fixture
def product_2():
    return Product("Клубника", "Ягода", 201.9, 5)


@pytest.fixture
def category_1():
    return Category("Сладости", "Для детей", ["Яблочное пюре", "Запеканка", "Сок", "Мороженное"])


@pytest.fixture
def category_2():
    return Category("Овощи", "ЗОЖ", ["Помидор", "Кабачок", "Тыква"])


@pytest.fixture
def category_3():
    return Category(
        "Ягоды", "Летний сезон", [Product("Малина", "Ягода", 159.1, 15), Product("Голубика", "Ягода", 267.7, 3)]
    )


@pytest.fixture
def category_4():
    return Category("Ягоды", "Летний сезон", [])


@pytest.fixture
def product_dict_1():
    return {"name": "Ежевика", "description": "Ягода", "price": 211.4, "quantity": 7}


@pytest.fixture
def smartphone_1():
    return Smartphone("Sumnum", "Смартфон", 15000, 5, 70, "A15", "2Gb", "black")


@pytest.fixture
def lawngrass_1():
    return LawnGrass("grass", "пушистая", 3015, 2, "Россия", "15 суток", "изумруд")


@pytest.fixture
def product_error_1():
    return Product("Рис", "Крупа", 75.5, 0)


@pytest.fixture
def product_error_2():
    return Product("Рис", "Крупа", 75.5, -3)
