class Product:
    """Создание класса Product"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            print("Цена понизилась? Да ладно!!! А чё так можно было?!!")
            return
        self.__price = new_price


# if __name__ == "__main__":
#     product1 = Product( "Samsung Galaxy C23 Ultra",
#         "256GB, Серый цвет, 200MP камера",
#         180000.0,
#         5)
#     print(product1.name)
#     print(product1.description)
#     print(product1.price)
#     print(product1.quantity)
#
#     product2 = Product.new_product("Iphone 15",
#         "512GB, Gray space",
#         210000.0,
#         8)
#     print(product2.name)
#     print(product2.description)
#     print(product2.price)
#     print(product2.quantity)
#
#     product2.price = 100000
#     print(product2.price)
