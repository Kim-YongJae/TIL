import sqlite3
from library.AbstractConnectionCreator import *

class ConnectionCreator(AbstractConnectionCreator):
    def getConnection(self):
        return sqlite3.connect('test_strategy.db', isolation_level=None)