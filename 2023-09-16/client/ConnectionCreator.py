import sqlite3


class ConnectionCreator():
    def getConnection(self):
        return sqlite3.connect('test_strategy.db', isolation_level=None)