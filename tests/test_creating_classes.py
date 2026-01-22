import pytest

from src.creating_classes import Category, Product


def test_init_product_1(product_1):
    assert product_1.name == "Рис"
    assert product_1.description == "Крупа"
    assert product_1.price == 75.5
    assert product_1.quantity == 10


def test_init_product_2(product_2):
    assert product_2.name == "Клубника"
    assert product_2.description == "Ягода"
    assert product_2.price == 201.9
    assert product_2.quantity == 5


def test_init_category_1(category_1):
    assert category_1.name == "Сладости"
    assert category_1.description == "Для детей"
    assert category_1.products_in_list == ["Яблочное пюре", "Запеканка", "Сок", "Мороженное"]
    assert Category.category_count == 1
    assert Category.product_count == 4


def test_init_category_2(category_1, category_2):
    assert category_2.name == "Овощи"
    assert category_2.description == "ЗОЖ"
    assert category_2.products_in_list == ["Помидор", "Кабачок", "Тыква"]
    assert Category.category_count == 3
    assert Category.product_count == 3


def test_setter_product_1(product_1):
    product_1.price = 15
    assert product_1.price == 15


def test_setter_product_2(capsys, product_1):
    product_1.price = -3
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"


def test_new_product(product_dict_1):
    assert Product.new_product(product_dict_1).name == "Ежевика"
    assert Product.new_product(product_dict_1).description == "Ягода"
    assert Product.new_product(product_dict_1).price == 211.4
    assert Product.new_product(product_dict_1).quantity == 7


def test_property_category(category_3):
    assert category_3.products == "Малина, 159.1 руб. Остаток: 15 шт.\nГолубика, 267.7 руб. Остаток: 3 шт.\n"


def test_add_product_category(category_3, product_2):
    category_3.add_product(product_2)
    assert category_3.products == (
        "Малина, 159.1 руб. Остаток: 15 шт.\n"
        "Голубика, 267.7 руб. Остаток: 3 шт.\n"
        "Клубника, 201.9 руб. Остаток: 5 шт.\n"
    )
    assert category_3.product_count == 3


def test_product_str(product_1):
    assert str(product_1) == "Рис, 75.5 руб. Остаток: 10 шт."


def test_product_add(product_1, product_2):
    assert product_1 + product_2 == 1764.5


def test_product_add_error(product_1, category_3):
    with pytest.raises(TypeError):
        i = product_1 + category_3


def test_category_str(category_3):
    assert str(category_3) == "Ягоды, количество продуктов: 18 шт."
