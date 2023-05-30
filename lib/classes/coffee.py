class Coffee:
    def __init__(self, name):
        if isinstance(name, str):
            self._name = name
        self._orders = []
        self._customers = []

    def get_coffee(self):
        return self._name
    
    def set_coffee(self, name):
        if hasattr(self, '_name'):
            raise Exception
        else:
            if isinstance(name, str):
                self._name = name
    
    name = property(get_coffee, set_coffee)
        
    def orders(self, new_order=None):
        from classes.order import Order
        if isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        if new_customer and isinstance(new_customer, Customer) and new_customer not in self._customers:
            self._customers.append(new_customer)
        return self._customers
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        price_list = []
        for each in self._orders:
            price_list.append(each.price)
        return sum(price_list) / len(price_list)
