# from src.category import Category
# from src.products import Product
#


class ProductIterator:
    """Итератор для перебора по списку товаров в категории"""

    def __init__(self, category_obj):
        self.category = category_obj
        self.start = 0

    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):
        if self.start < len(self.category.products_list):
            product = self.category.products_list[self.start]
            self.start += 1
            return product
        else:
            raise StopIteration


#
# if __name__ == "__main__":
#     product1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     electronics = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
#         [product1, product2],
#     )
#     iterator = ProductIterator(electronics)
#
#     for product in iterator:
#         print(product)
