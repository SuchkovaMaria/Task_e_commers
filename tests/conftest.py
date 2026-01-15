import pytest

from src.creating_classes import Category, Product


@pytest.fixture
def product_1():
    return Product("Рис", "Крупа", 75.5, 10)


@pytest.fixture
def product_2():
    return Product("Клубника", "Ягода", 201.9, 5)


# @pytest.fixture
# def product_3():
#     return Product("Малина", "Ягода", 159.1, 15)
#
# @pytest.fixture
# def product_4():
#     return Product("Голубика", "Ягода", 267.7, 3)


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
def product_dict_1():
    return {"name": "Ежевика", "description": "Ягода", "price": 211.4, "quantity": 7}
