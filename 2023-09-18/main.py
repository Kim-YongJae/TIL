from User import *
from Calculator import *

if __name__ == '__main__':
    user = User.UserBuilder().name('hmd')\
        .email('hmd@hdm.com')\
        .password('123abc')\
        .tell('010-0000-0000')\
        .build()
        
    print(user)
    
    calculator = Calculator(10).add(10).add(10).subtract(5).divide(3).end()
    print('(10 + 10 + 10 - 5) / 3 =', calculator)