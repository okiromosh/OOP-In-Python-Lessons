"""

    1. Certain class can inherit attributes from other classes
        Example
            class Item:
                pass
            class Phone(Item)
                pass
        The class Phone will inherit the attributes  from Item eg. name, price,
            quantity and all the methods too
    2. This is useful when certain instances have additional methods that are only
        used by them. eg. phone1.phone_broken.
        This method only applies to instances of phone but not others, yet phones inherit
            attributes like name, price, quantity

           PARENT CLASS
             |
    3. class Store:                     # All items in the store will always have these attributes and
            Attribute- Name                 methods
                       Price
                       Quantity
            Methods-    Discount
            CHILD CLASS
              |
        class Phone(Store):             # This class will have attributes only phones have
            Attributes - Brand              + inherited attributes from Store
                         RAM
                         Storage

        class Televisions(Store):         # Television ony attributes + Inherited attributes
            Attributes -Brand
                        Screen_Size
    4. To inherit the class attributes, we use the Super function
            super().__init__(name, price, quantity)

"""

import csv


class Item:
    pay_rate = 0.8  # Class level attribute
    all = []

    def __init__(self, name: str, price: int, quantity=0):
        # Assign attributes
        self.name = name  # Instance level attribute
        self.price = price
        self.quantity = quantity

        # Validate received arguments
        assert price >= 0, f"Price {price} is a Negative Value!"
        assert quantity >= 0, f"Quantity {quantity} is a Negative Value!"

        # Actions to execute
        Item.all.append(self)  # Item attribute <all> receives every created instance(self)

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
        return f"Item('{self.name}', {self.price}, {self.quantity})"


class Phone(Item):

    def __init__(self, name: str, price: int, quantity=0, broken_phones=0):
        # Call to Super function to have access to parent attributes and methods
        super().__init__(name, price, quantity)

        # Assign to objects
        self.broken_phones = broken_phones

        # Validate received args
        assert broken_phones >= 0, f"Broken Phone {broken_phones} is a Negative"


phone1 = Phone("jcPhonev10", 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("jcPhonev20", 700, 5, 1)

"""
    1. In representation with inheritance, we use a magic method to get specific class 
        name for each instance.
            {self.__class__.__name__}
    2. Always use the all attribute only in Parent class
"""