from library.Developer import *
from library.ProxyDeveloper import *

class Woman(Developer):
    
    def __new__(cls):
        return ProxyDeveloper(super().__new__(cls))
    
    def develop(self):
            print('파이썬으로 개발한다.')
        