class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book: {self.title} by {self.author} - ₹{self.price}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.price})"


b1 = Book("Python Basics", "John", 500)
b2 = Book("OOP Mastery", "David", 750)

print(b1)          
print([b1, b2])    