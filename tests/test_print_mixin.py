from src.lawngrass import LawnGrass
from src.products import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys):
    """тест выводного сообщения через mixin"""

    Product("Игровая консоль", "Sony Playstation 5", 100000.00, 10)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Игровая консоль, Sony Playstation 5, 100000.0, 10)"

    Smartphone(
        "Samsung Galaxy C23 Ultra",
        "256GB,Серый цвет, 200MP камера",
        180000.0,
        1,
        "2,50 Ghz",
        "C23 Ultra",
        "256GB",
        "Black",
    )
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung Galaxy C23 Ultra, 256GB,Серый цвет, 200MP камера, 180000.0, 1)"

    LawnGrass("Ну трава...", "Да, блин, трава и всё", 1000.0, 10, "РФ", "30 дней", "Угадай(ответ: зелёная)")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Ну трава..., Да, блин, трава и всё, 1000.0, 10)"
