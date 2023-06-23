class Item:  # This creates a class with name Item

    pay_rate = 0.8                  # Class level attribute

    def __init__(self, name: str, price: int, quantity=0):
        # Assign attributes
        self.name = name            # Instance level attribute
        self.price = price
        self.quantity = quantity

        # Validate received arguments
        assert price >= 0, f"Price {price} is a Negative Value!"
        assert quantity >= 0, f"Quantity {quantity} is a Negative Value!"

    def calculate_total_price(self, ):
        return self.price * self.quantity

    def apply_discount(self):
        """
        1. When calling a  level attributes, define it using object_name.attribute_name
                Item.pay_rate, self.pay_rate
                If you use Item.pay_rate, the class level value  becomes default regardless of any changes
                If you use self.pay_rate, python first searches for any Instance level value, if it doesn't find
                 one, then it uses the Class level value.

        2. self.price = self.price * Item.pay_rate
           self.price = self.price * self.pay_rate
            (<new instance price> is equal to <given instance price> multiply by <pay_rate value>

        """

        self.price = self.price * self.pay_rate


item1 = Item("Phone", 500, 5)
print(f"item1 price: {item1.price}")
item1.apply_discount()  # Any price changes only occur if discount method is called
print(f"item1 price after discount: {item1.price}\n"
      f"This uses the Class level pay_rate value because  we haven't defined an instance value")
print()

item2 = Item("Laptop", 1000, 3)
print(f"item2 price: {item2.price}")
item2.pay_rate = 0.7  # This creates a unique value for the attribute at the instance level
item2.apply_discount()
print(f"item2 price after discount: {item2.price}\n"
      f"This uses the Instance level pay_rate value because  we defined an instance value")
print()

"""
    __dict__
    Builtin magic attribute
        displays all attributes belonging to that object

print(Item.__dict__)            # All attributes at Class level
print(item1.__dict__)           # All attributes at Instance level
"""
"""
        NOTES
    Python always looks for attribute values at Instance level first then Class level next
"""

