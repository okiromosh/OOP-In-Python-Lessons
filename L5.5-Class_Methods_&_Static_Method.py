

class Item:
    @staticmethod
    def is_integer(num):
        """
            1. This should do something that has a relationship
                with the class, but not something that must be
                unique per instance.
                Might be used by the class, but not important to the class.
            2. This method can be used outside the class without issue.

        """

    @classmethod
    def instantiate_from_something(cls):
        """
            1. This should also do something that has a relationship
                with the class, but usually,
                These are used to manipulate different data structures
                to instantiate objects. ie. like from
                            csv file, json file, yaml  file
            2. This method allows us to create objects within the class
                not from outside the class, say using a csv file to
                create/instantiate objects. ie. from csv data table,
                create item1, item2
            3. Before then, we were creating item1, item2 outside of the
                class.
        """