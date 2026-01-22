def test_init_smartphone_1(smartphone_1):
    """Создание экземпляра класса Смартфон"""

    assert smartphone_1.name == "Sumnum"
    assert smartphone_1.description == "Смартфон"
    assert smartphone_1.price == 15000
    assert smartphone_1.quantity == 5
    assert smartphone_1.efficiency == 70
    assert smartphone_1.model == "A15"
    assert smartphone_1.memory == "2Gb"
    assert smartphone_1.color == "black"


def test_init_lawnGrass_1(lawngrass_1):
    """Создание экземпляра класса Трава газонная"""

    assert lawngrass_1.name == "grass"
    assert lawngrass_1.description == "пушистая"
    assert lawngrass_1.price == 3015
    assert lawngrass_1.quantity == 2
    assert lawngrass_1.country == "Россия"
    assert lawngrass_1.germination_period == "15 суток"
    assert lawngrass_1.color == "изумруд"
