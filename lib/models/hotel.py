# lib/models/hotel.py
from models.__init__ import CURSOR, CONN

class Hotel:
    all = {}

    def __init__(self, name, location, services):
        self.name = name
        self.location = location
        self.services = services

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        
    @property
    def location(self):
        return self._location
    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location)>0:
            self._location = location
        else:
            raise ValueError("Location must not be an empty string")
        
    @property
    def services(self):
        return self._services
    @services.setter
    def services(self, services):
        if isinstance(services, str) and len(services):
            self._services
        else:
            raise ValueError("Services must be a non empty string")
        

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS hotels(
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT,
            services TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS hotels;
        """
        CURSOR.execute(sql)
        CONN.commit()
