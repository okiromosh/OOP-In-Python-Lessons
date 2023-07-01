import csv


class Item:
    pay_rate = 0.8  # Class level attribute
    """
        all attribute:
    """
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
        """
        1.This method cant call the (self)  because its supposed to create the instances,
            thus we convert this method to a Class Method
        2. Class Method: can only be accessed from the class level
                Item.instantiate_from_csv()
        3. To convert a method to a Class Method, we use the decorator @classmethod
        4. Once converted, it will receive the parameter (cls), thus this method will call the Class as
            the first argument

        """
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

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


# Item.instantiate_from_csv()
print(Item.all)


"""
    CSV
        Comma Separated Values
"""