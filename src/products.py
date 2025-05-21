from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Создание класса Product"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализатор класса"""

        self.name = name
        self.description = description
        self.__price = price
        try:
            if quantity != 0:
                self.quantity = quantity
            else:
                raise ValueError
        except ValueError:
            self.quantity = quantity
            print("Товар с нулевым количеством не может быть добавлен.")

        super().__init__()  # обращение к родительскому классу

    def __str__(self):
        """Представление экземпляров класса Product в строковом формате"""
        return f"{self.name}, {self.price}, Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод сложения экземпляров(складывается цена, умноженная на количество"""
        if type(other) is Product:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, name, description, price, quantity):
        """класс-метод добавления продукта"""
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер для обращения к приватному атрибуту __price"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер атрибута с проверкой условий, что цена не нулевая, не отрицательная, не меньше предыдущей"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            print("Цена понизилась? Да ладно!!! А чё так можно было?!!")
            return
        else:
            self.__price = new_price


# if __name__ == "__main__":
#     product1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     print(product1.name)
#     print(product1.description)
#     print(product1.price)
#     print(product1.quantity)
#
#     product2 = Product.new_product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     print(product2.name)
#     print(product2.description)
#     print(product2.price)
#     print(product2.quantity)
#
#     product2.price = 100000
#     print(product2.price)
#     print(product1 + product2)
