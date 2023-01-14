import sqlite3
from sqlite3 import Connection


# Setting up connection
class DataBase:
    def __init__(self, path: str):
        self.path = path

    def connect(self) -> Connection:
        return sqlite3.connect(self.path)
