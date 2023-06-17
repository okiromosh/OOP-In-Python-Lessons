class Item:  # This creates a class with name Item
    """
     Creating a method in the class Item
     The method will receive 3 parameters/arguments (self, x, y)
        self represents the instance
        x represents variable one
        y represents variable two
    """

    def calculate_total_price(self, x, y):  #
        return x * y


item1 = Item()  # This creates an instance of the class Item
print(type(item1))  # <class '__main__.Item'>


"""
    Assigning attributes the the instance
"""
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
"""
    Assigning a method to the instance
    (self) argument will be item1
    The method will need two more arguments,
    (x) argument will be price
    (y) argument will be quantity

"""
"""
   item1.calculate_total_price(item1.price, item1.quantity)
      |                                |            |
    self                               x            y
"""

print(item1.calculate_total_price(item1.price, item1.quantity))     # 500


item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3

print(item2.calculate_total_price(item2.price, item2.quantity))     # 3000


"""
            NOTES
    def :
        outside of class are called functions
        inside of a class are called methods

    Any method created will always have (self) as a parameter except methods with
        class decorator (LESSON 5) and
        static decorator (LESSON 6)
"""



