def test_mixin_print_1(capsys, product_2):
    massage = capsys.readouterr()
    assert massage.out.strip() == "Product, , Клубника, Ягода, 201.9, 5"


def test_mixin_print_2(capsys, smartphone_1):
    massage = capsys.readouterr()
    assert massage.out.strip() == "Smartphone, , Sumnum, Смартфон, 15000, 5"
