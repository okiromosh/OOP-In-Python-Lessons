class Item:  # This creates a class with name Item
    def __init__(self, name: str, price: int, quantity=0):
        """
        1. __init__(self)
                Is auto called whenever an instance of the class is called
                (self) argument is any and all instances created. eg. item1, item2

        2. Always assign the attributes inside the __init__ method

        3. You can assign a default value to an argument
                def __init__(self, name, price, quantity=0)
        4. You can assign data types to your arguments
                (name: str)

                * when you assign a default value, your argument inherits the values type

        5. self.name = name
              |        |
           attribute  argument
          <instance.attribute =  argument>
        """

        # Assign attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        # Validate received arguments
        assert price >= 0, f"Price {price} is a Negative Value!"
        assert quantity >= 0, f"Quantity {quantity} is a Negative Value!"


    def calculate_total_price(self,):
        """
        We just call the attributes without assigning arguments
         because we've already assigned them in __init__

        """
        return self.price * self.quantity


"""
    Creating an instance of class Item
    Assign the arguments required by the __init__ method ie, (name, price, quantity)
"""
item1 = Item("Phone", 500, 5)
item2 = Item("Laptop", 1000, 3)

"""
    You can assign specific attributes to individual instances
    item2.has_numpad = False
"""


print(f"Name:{item1.name}, Price:{item1.price}, Quantity:{item1.quantity}")
print(f"Name:{item2.name}, Price:{item2.price}, Quantity:{item2.quantity}")


print(f"Total: {item1.calculate_total_price()}")
print(f"Total: {item2.calculate_total_price()}")




"""
            NOTES
    def :
        outside of class are called functions
        inside of a class are called methods

    Any method created will always have (self) as a parameter
"""
