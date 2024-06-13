# lib/models/client.py
from models.__init__ import CURSOR, CONN

class Client:
    all = {}

    def __init__(self, name, address, needs, id= None):
        self.id = id
        self.name = name
        self.address = address
        self.needs = needs

    def __repr__(self):
        return f"<Client {self.id}: {self.name}, {self.address}, {self.needs}>"

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance (name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must not be an empty string")
        
    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, address):
        if isinstance(address, str) and len(address):
            self._address = address

    @property
    def needs(self):
        return self._needs
    @needs.setter
    def needs(self, needs):
        if isinstance(needs, str):
            self._needs = needs
        else:
            raise ValueError("Service required must be a string")
        

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS clients(
            id INTEGER PRIMARY KEY,
            name TEXT,
            address TEXT,
            needs TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS clients;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO clients (name, address, needs) VALUES (?,?,?)
        """
        CURSOR.execute(sql, (self.name, self.address, self.needs))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, address, needs):
        client = cls(name, address, needs)
        client.save()
        return client
