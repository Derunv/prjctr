class Product():
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)


class Book(Product):
    def __init__(self, name: str, price: float, quantity: int, author: str):
        self.author = author
        Product.__init__(self, name, price, quantity)

    def read(self):
        return self.name, self.price, self.author

book_1984 = Book('1984', 253, 5, 'J. Orvell')
print(book_1984.read())
