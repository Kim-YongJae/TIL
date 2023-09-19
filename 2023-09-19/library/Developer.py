from abc import *

class Developer(metaclass = ABCMeta):
    
    @abstractmethod
    def develop(self):
        pass