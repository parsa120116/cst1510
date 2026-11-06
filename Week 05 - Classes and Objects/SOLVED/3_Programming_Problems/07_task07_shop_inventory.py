class Product:
    """A product in a shop, with a price and a quantity in stock."""

    def __init__(self, name, price, quantity):
        """Store the product details."""
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        """Return price x quantity for this product."""
        return self.price * self.quantity

    def apply_discount(self, percent):
        """Lower this product's own price by the given percent."""
        self.price = self.price * (1 - percent / 100)


inventory = [
    Product("Laptop", 800.00, 3),
    Product("Mouse", 20.00, 25),
    Product("Keyboard", 45.00, 10),
    Product("Monitor", 150.00, 4),
    Product("USB cable", 5.00, 40),
]

# 1. Total value of the whole inventory
total = 0
for product in inventory:
    print(f"{product.name}: {product.quantity} x {product.price:.2f} = {product.total_value():.2f}")
    total += product.total_value()
print(f"Total inventory value: {total:.2f}")

# 2. 10% off everything
print()
print("After a 10% discount:")
for product in inventory:
    old_price = product.price
    product.apply_discount(10)
    print(f"{product.name}: {old_price:.2f} -> {product.price:.2f}")

new_total = 0
for product in inventory:
    new_total += product.total_value()
print(f"New total inventory value: {new_total:.2f}")
