"""
                ENCAPSULATION
        1. Refers the the concept of restricting the direct access the some
            attributes in a program.

            Cannot apply changes directly but by methods eg.

            @property                                   # Stops direct change once value is set
        def price(self):
            return self.__price

        def apply_discount(self):                       # Any changes made will be allowed
            self.__price = self.__price * self.pay_rate

        def apply_increment(self, increment_value):     # Any changes made will be allowed
            self.__price = self.__price + self.__price * increment_value


                ABSTRACTION
        1. OOP concept that show the necessary attributes and hides the unnecessary
            attributes.
            Hide unnecessary details from the user
        2. In a normal occurrence, a user could call the method
                item1.connect
             which is a background process
        3. This is archived by adding double underscore to the method name
                def __connect(self):


                INHERITANCE
        1. Concept that allows us to reuse code (methods and attributes) across our classes
        2. Refer to L7-Inheritance.py
        3. For example, without rewriting code.
            Phone class can call the apply_increment method
                             or the send_email method



                POLYMORPHISM

        1. Means the same function name(but different signatures) being
            used for different types
        2. Example
                word = "geeks"
                print(len(word))        >5

                list = [10, 20. 30]
                print(len(list))        >3

            The function len can be used to different types

        3. Does apply to inherited class methods too.




"""

import csv


class Item:
    pay_rate = 0.8  # Class level attribute
    all = []

    def __init__(self, name: str, price: int, quantity=0):
        # Assign attributes
        self.__name = name  # Instance level attribute
        self.__price = price
        self.quantity = quantity

        # Validate received arguments
        assert price >= 0, f"Price {price} is a Negative Value!"
        assert quantity >= 0, f"Quantity {quantity} is a Negative Value!"

        # Actions to execute
        Item.all.append(self)  # Item attribute <all> receives every created instance(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    # Property Decorator = Read Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def calculate_total_price(self, ):
        return self.__price * self.quantity

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
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    # All processes to send email
    def __connect(self, smtp_server):
        pass

    def __prepare_body(self):
        return f"""
            Hello Someone
            We have {self.name} {self.quantity} times.
            Regards Mosh
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()
