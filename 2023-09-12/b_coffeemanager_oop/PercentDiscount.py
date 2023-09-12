from Order import *

class PercentDiscount:
    @staticmethod
    def cal_discount_order_price(order_price):
        discount = 0

        if order_price >= 10000:
            discount = int(order_price * 0.1)
            
        return discount
            