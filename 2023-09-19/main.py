from client.Child import *
from client.Man import *
from client.Woman import *

if __name__ == '__main__':
    man = Man()
    man.develop()
    print()
    
    woman = Woman()
    woman.develop()
    print()
    
    child = Child()
    child.develop()