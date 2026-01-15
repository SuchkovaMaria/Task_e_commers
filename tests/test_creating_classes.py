from src.creating_classes import Category


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
    assert category_1.products == ["Яблочное пюре", "Запеканка", "Сок", "Мороженное"]
    assert Category.category_count == 1
    assert Category.product_count == 4


def test_init_category_2(category_1, category_2):
    assert category_2.name == "Овощи"
    assert category_2.description == "ЗОЖ"
    assert category_2.products == ["Помидор", "Кабачок", "Тыква"]
    assert Category.category_count == 3
    assert Category.product_count == 3
