class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 100, 1)

item2 = Item("Laptop", 1000, 3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

# accessing to class atributes
print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)

# Item.__dict__
print(Item.__dict__)  # class level
print(item1.__dict__)  # instance level
