class Coffee:
    def __init__(self, name):
        self.name = name
        self.orders_list = []
        self._customer_list = []

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, '_name'):
            self._name = name
        else:
            raise Exception
        
    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and isinstance(new_order, Order):
            self.orders_list.append(new_order)
        return self.orders_list
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        if new_customer and isinstance(new_customer, Customer) and new_customer not in self._customer_list:
            self._customer_list.append(new_customer)
        return self._customer_list
    
    def num_orders(self):
        return len(self.orders_list)
    
    def average_price(self):
        price_list = []
        for each in self.orders_list:
            price_list.append(each.price)
        return sum(price_list) / len(price_list)