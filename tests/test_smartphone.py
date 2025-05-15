import pytest


def test_smartphone_init(smartphone1):
    """тест инициализации экземпляра класса Smartphone"""
    assert smartphone1.name == "Samsung Galaxy C23 Ultra"
    assert smartphone1.description == "256GB,Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 1
    assert smartphone1.efficiency == "2,50 Ghz"
    assert smartphone1.model == "C23 Ultra"
    assert smartphone1.memory == "256GB"
    assert smartphone1.color == "Black"


def test_smartphone_add(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == 390000.0


def test_smartphone_add_error(smartphone1, grass1):
    with pytest.raises(TypeError):
        smartphone1 + grass1
