from classes.coffee import Coffee
from classes.order import Order

class Customer:
    def __init__(self, name):
        self.name = name
        self.order_list = []
        self._coffee_list = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception

    def orders(self, new_order=None):

        if new_order and isinstance(new_order, Order):
            self.order_list.append(new_order)
        return self.order_list

    def coffees(self, new_coffee=None):

        if new_coffee and isinstance(new_coffee, Coffee) and new_coffee not in self._coffee_list:
            self._coffee_list.append(new_coffee)
        return self._coffee_list

    def create_order(self, coffee, price):

        if isinstance(coffee, Coffee) and isinstance(price, int):
            new_order = Order(self, coffee, price)
            self.orders(new_order)
            return new_order