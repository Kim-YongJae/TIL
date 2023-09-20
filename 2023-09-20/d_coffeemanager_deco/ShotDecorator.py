from Coffee import *

class ShotDecorator(Coffee):
    def __init__(self, coffee):
        super().__init__(coffee._name,
                         coffee._stock,
                         coffee._total_sales_cnt,
                         coffee._safety_stock,
                         coffee._cost,
                         coffee._price)
        
        self.__coffee = coffee
        self.__name = self.__coffee.get_name() + '[shot]'
        self.__topping_price = 500
        
    def offer(self, order_cnt):
        self.__coffee.offer(order_cnt)

    def add_stock(self, cnt):
        self.__coffee.add_stock(cnt)
        
    def get_stock(self):
        return self.__coffee.get_stock()
    
    def get_total_sales_cnt(self):
        return self.__coffee.get_total_sales_cnt()
        
    def get_price(self):
        return self.__coffee.get_price() + self.__topping_price
    
    def get_name(self):
        return self.__name
    
    def __str__(self):
        return str(super()) + self.__name