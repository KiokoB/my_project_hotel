# lib/models/hotel.py
from models.__init__ import CURSOR, CONN

class Hotel:
    all = {}

    def __init__(self, name, location, contact):
        self.name = name
        self.location = location
        self.contact = contact

    def __repr__(self):
        return f"<Hotel {self.id}: {self.name}, {self.location}, {self.contact}>"


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
    def contact(self):
        return self._contact
    @contact.setter
    def contact(self, contact):
        if isinstance(contact, str) and len(contact):
            self._contact = contact
        else:
            raise ValueError("Contact must be a non empty string")
        

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS hotels(
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT,
            contact TEXT)
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

    def save(self):
        sql = """
            INSERT INTO hotels (name, location, contact) VALUES (?,?,?)
        """
        CURSOR.execute(sql, (self.name, self.location, self.contact))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, location, contact):
        hotel = cls(name, location, contact)
        hotel.save()
        return hotel
    
    def update(self):
        sql = """
            UPDATE hotels
            SET name = ?, location = ?, contact = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.contact, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM hotels
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        hotel = cls.all.get(row[0])
        if hotel:
            hotel.name = row[1]
            hotel.location = row[2]
            hotel.contact = row[3]
        else:
            hotel = cls(row[1],row[2],row[3])
            hotel.id = row[0]
            cls.all[hotel.id] = hotel
        return hotel
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * 
            FROM hotels
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls,id):
        sql = """
            SELECT *
            FROM hotels
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls,name):
        sql = """
            SELECT *
            FROM hotels
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def employees(self):
        from models.employee import Employee
        sql = """
            SELECT * FROM employees
            WHERE hotel_id = ?
        """
        CURSOR.execute(sql,(self.id,),)
        rows = CURSOR.fetchall()
        return [
            Employee.instance_from_db(row) for row in rows
        ]

    def clients(self):
        from models.client import Client
        sql = """
            SELECT * FROM clients
            WHERE hotel_id = ?
        """
        CURSOR.execute(sql,(self.id,),)
        rows = CURSOR.fetchall()
        return [
            Client.instance_from_db(row) for row in rows
        ]

    