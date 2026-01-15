import pytest

from src.creating_classes import Category, Product


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
