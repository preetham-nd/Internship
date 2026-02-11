class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value


cart = ShoppingCart(["Shirt", "Shoes", "Watch"])

print(cart[0])
cart[1] = "Sneakers"
print(cart.items)