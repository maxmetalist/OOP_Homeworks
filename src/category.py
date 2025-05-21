# from src.lawngrass import LawnGrass

from src.exceptions import ZeroQuantityError
from src.products import Product

# from src.smartphone import Smartphone


class Category:
    """Создание класса Category с параметром products, являющимся списком
    экземпляров класса Product"""

    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products=None):
        """Инициализатор объектов класса"""

        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        """Представление экземпляра класса Category в строковый формат"""
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def add_product(self, product):
        """Метод для добавления товаров"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для обращения к атрибуту products"""
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @products.setter
    def products(self, product: Product):
        """Сеттер для преобразования атрибута products
        (добавлялась проверка на принадлежность объекта классу Product"""
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityError(
                        "Круто, конечно, но у тебя количество ноль." "Как мы добавим дырку от бублика?"
                    )
            except ZeroQuantityError as error:
                print(str(error))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Ладно, так и быть. Товар добавлен.")
            finally:
                print("Обработка завершена. Как то так...")
        else:
            raise TypeError

    @property
    def products_list(self):
        """Геттер для обращения к преобразованному в список атрибуту products"""
        return self.__products

    def middle_price(self):
        """Метод для вычисления средней цены товара в категории"""
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            print("Делить на ноль?!!!?? Да ты гений математики! Лобачевский нервно курит.")
            return 0


# if __name__ == '__main__':
#     product1 = Product("Samsung Galaxy S23 Ultra",
#                        "256GB, Серый цвет, 200MP камера",
#                        180000.0,
#                        5)
#     product2 = Product("Iphone 15",
#                        "512GB, Gray space",
#                        210000.0,
#                        8)
#     product3 = Product("Xiaomi Redmi Note 11",
#                        "1024GB, Синий",
#                        31000.0,
#                        14)
#
#     print(product1.name)
#     print(product1.description)
#     print(product1.price)
#     print(product1.quantity)
#
#     print(product2.name)
#     print(product2.description)
#     print(product2.price)
#     print(product2.quantity)
#
#     print(product3.name)
#     print(product3.description)
#     print(product3.price)
#     print(product3.quantity)
#
#     category1 = Category("Смартфоны",
#                          "Смартфоны, как средство не только коммуникации,"
#                          "но и получения дополнительных функций для удобства жизни",
#                          [product1, product2, product3])
#
#     print(category1.name == "Смартфоны")
#     print(category1.description)
#     print(len(category1.products))
#     print(category1.category_count)
#     print(category1.product_count)
#
#     product4 = Product("55\" QLED 4K",
#                        "Фоновая подсветка",
#                        123000.0,
#                        7)
#     category2 = Category("Телевизоры",
#                          "Современный телевизор, который позволяет"
#                          "наслаждаться просмотром, станет вашим другом и помощником",
#                          [product4])
#
#     print(category2.name)
#     print(category2.description)
#     print(len(category2.products))
#     print(category2.products)
#
#     print(Category.category_count)
#     print(Category.product_count)
#
# if __name__ == '__main__':
#     try:
#         product_invalid = Product("Бракованный товар",
#                                   "Неверное количество",
#                                   1000.0,
#                                   0)
#     except ValueError as e:
#         print(
#             "Возникла ошибка ValueError прерывающая работу программы"
#             "при попытке добавить продукт с нулевым количеством")
#     else:
#         print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")
#
#     product1 = Product("Samsung Galaxy S23 Ultra",
#                        "256GB, Серый цвет, 200MP камера",
#                        180000.0,
#                        5)
#     product2 = Product("Iphone 15",
#                        "512GB, Gray space",
#                        210000.0,
#                        8)
#     product3 = Product("Xiaomi Redmi Note 11",
#                        "1024GB, Синий",
#                        31000.0,
#                        14)
#
#     category1 = Category("Смартфоны",
#                          "Категория смартфонов",
#                          [product1, product2, product3])
#
#     print(category1.middle_price())
#
#     category_empty = Category("Пустая категория",
#                               "Категория без продуктов",
#                               [])
#     print(category_empty.middle_price())
#
# if __name__ == "__main__":
#     product = Product("Кирпич",
#                       "Брак бракованый",
#                       1000.0,
#                       0)
#     category = Category("Смартфоны",
#                          "Смартфоны, как средство не только коммуникации,"
#                          "но и получения дополнительных функций для удобства жизни",
#                         [product])
#     print(category.name)
#     print(category.description)
#     print(category)
#     category.products = product
