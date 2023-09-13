from library.AbstractDAO import *
import sqlite3

class DAO(AbstractDAO):
    def getConnection(self):
        return sqlite3.connect('template_method.db', isolation_level=None)