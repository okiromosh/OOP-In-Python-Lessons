class Item:
    pay_rate = 0.8  # Class level attribute
    all = []            # Variable to contain created instances (item1, item2)

    def __init__(self, name: str, price: int, quantity=0):
        # Assign attributes
        self.name = name  # Instance level attribute
        self.price = price
        self.quantity = quantity

        # Validate received arguments
        assert price >= 0, f"Price {price} is a Negative Value!"
        assert quantity >= 0, f"Quantity {quantity} is a Negative Value!"

        # Actions to execute
        Item.all.append(self)       # Item attribute <all> receives every created instance(self)

    def calculate_total_price(self, ):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        """
        Using the represent method allows us to display class objects visually instead of object location
        print(Item.all)
            without __repr__
                    [<__main__.Item object at 0x7f692db73e80>]
            with __repr__
                    [Item('Phone', 100, 1)]
        """
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
