class Product:
    """
    Класс для описания товара в магазине
    """
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            product_data['name'],
            product_data['description'],
            product_data['price'],
            product_data['quantity']
        )
    # def new_product(cls, name: str, description: str, price: float, quantity: int):
    #     return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return
        else:
            self.__price = new_price




class Category:
    """
    Класс для категорий товара
    """
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.__product_list = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    @property
    def products(self):
        prod_str = ''
        for product in self.__product_list:
            prod_str += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return prod_str

    @products.setter
    def products(self, product: Product):
        self.__product_list.append(product)
        Category.product_count += 1


if __name__ == '__main__':
    data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8
                },
                {
                    "name": "Xiaomi Redmi Note 11",
                    "description": "1024GB, Синий",
                    "price": 31000.0,
                    "quantity": 14
                }
            ]
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "products": [
                {
                    "name": "55 QLED 4K",
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7
                }
            ]
        }
    ]

    categories = []
    for category in data:
        products = []
        for product in category['products']:
            print(product)
            products.append(Product.new_product(product))
        category['products'] = products
        categories.append(Category(**category))



    product_item = Product('Test', 'Test', 1000, 10)
    print(product_item.price)

    product_item.price = 800
    print(product_item.price)