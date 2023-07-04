
"""

                ENCAPSULATION
    1. Read Only Attributes:
     Attributes whose value once stated cannot be changed

    2. Read Only Attributes are defined by adding a single underscore
            self._name

    3. Read Only methods defined by a property decorator
            @property
            def name(self):
            return self._name
    4. The attribute can be changed by accessing the _name
            item1._name = "NewName"

    4. Private Attributes:
        Attributes not accessible outside the class.
        Defined by two  underscores
            self.__name

            @property
            def name(self):
            return self.__name

    5. To set a new value for a private attribute, we use the setter decorator
            @name.setter
            def name(self, value)
                self.__name = value

"""
import csv


class Item:
    pay_rate = 0.8  # Class level attribute
    all = []

    def __init__(self, name: str, price: int, quantity=0):
        # Assign attributes
        self.__name = name  # Instance level attribute
        self.price = price
        self.quantity = quantity

        # Validate received arguments
        assert price >= 0, f"Price {price} is a Negative Value!"
        assert quantity >= 0, f"Quantity {quantity} is a Negative Value!"

        # Actions to execute
        Item.all.append(self)  # Item attribute <all> receives every created instance(self)

    @property
    # Property Decorator = Read Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def calculate_total_price(self, ):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):

        with open('../items.csv') as f:  # Opens the csv file as a variable f
            reader = csv.DictReader(f)  # Variable reader contains data read by csv.DictReader from f
            items = list(reader)  # variable items converts readers data to a list format
        for item in items:
            # print(item)
            """
                To instantiate from the csv items
            """
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):  # Method to check if argument num is an integer

        if isinstance(num, float):  # Will check for .0 values i.e. 5.0, 10.0
            return num.is_integer()  # Returns True if its .0
        elif isinstance(num, int):  # Checks if num doesnt have a decimal
            return True  # Returns True
        else:
            return False  # Returns False if decimal is any other num i.e. .1, .9

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

