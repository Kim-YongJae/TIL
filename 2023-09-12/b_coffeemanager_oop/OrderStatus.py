from enum import Enum

# 연관된 상수들의 집합
class OrderStatus(Enum):
    # OK = OrderStatus(0, '주문 생성 성공')
    OK = (0, '주문 생성 성공')
    FAIL_CAUSE_SOLDOUT = (1, '품절로 인한 주문 실패')
    FAIL_CAUSE_STOCK = (2, '재고 부족으로 인한 주문 실패')
    COMPLITE = (4, '주문 완료')
    
    def __init__(self, code, desc):
        self.code = code
        self.desc = desc
    
    def check_order_status(order):
        
        coffee = order.get_coffee()
        order_cnt = order.get_order_cnt()
        
        if coffee.get_stock() < order_cnt:
            return OrderStatus.FAIL_CAUSE_STOCK
        else:
            return OrderStatus.OK
    
    def is_ok(self):
        return self == OrderStatus.OK
    
    def is_complete(self):
        return self == OrderStatus.COMPLITE
    
    def is_fail(self):
        return self in [OrderStatus.FAIL_CAUSE_SOLDOUT, OrderStatus.FAIL_CAUSE_STOCK]