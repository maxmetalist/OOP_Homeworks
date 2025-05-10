from src.products import Product


class Category:
    """Создание класса Category с параметром products, являющимся списком
    экземпляров класса Product"""

    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products=None):

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
        """Сеттер для преобразования атрибута products"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_list(self):
        """Геттер для обращения к преобразованному атрибуту products"""
        return self.__products


#
# if __name__ == "__main__":
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     print(str(product1))
#     print(str(product2))
#     print(str(product3))
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#
#     print(str(category1))
#
#     print(category1.products)
#
#     print(product1 + product2)
#     print(product1 + product3)
#     print(product2 + product3)
