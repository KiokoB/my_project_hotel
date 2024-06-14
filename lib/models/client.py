# lib/models/client.py
from models.__init__ import CURSOR, CONN
from models.hotel import Hotel

class Client:
    all = {}

    def __init__(self, name, address, needs, hotel_id, id= None):
        self.id = id
        self.name = name
        self.address = address
        self.needs = needs
        self.hotel_id = hotel_id

    def __repr__(self):
        return (
            f"<Client {self.id}: {self.name}, {self.address}, {self.needs}>, " +
            f"Hotel ID: {self.hotel_id}>"
        )

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
        
    @property
    def hotel_id(self):
        return self._hotel_id

    @hotel_id.setter
    def hotel_id(self, hotel_id):
        if type(hotel_id) is int and Hotel.find_by_id(hotel_id):
            self._hotel_id = hotel_id
        else:
            raise ValueError(
                "hotel_id must reference a hotel in the database")

        

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS clients(
            id INTEGER PRIMARY KEY,
            name TEXT,
            address TEXT,
            needs TEXT,
            hotel_id INTEGER,
            FOREIGN KEY(hotel_id) REFERENCES hotels(id))
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
            INSERT INTO clients (name, address, needs, hotel_id) VALUES (?,?,?,?)
        """
        CURSOR.execute(sql, (self.name, self.address, self.needs, self.hotel_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, address, needs, hotel_id):
        client = cls(name, address, needs, hotel_id)
        client.save()
        return client
    
    def update(self):
        sql = """
            UPDATE clients
            SET name = ?, address = ?, needs = ?, hotel_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.address, self.needs, self.hotel_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM clients
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        client = cls.all.get(row[0])
        if client:
            client.name = row[1]
            client.address = row[2]
            client.needs = row[3]
            client.hotel_id = row[4]
        else:
            client = cls(row[1],row[2],row[3],row[4])
            client.id = row[0]
            cls.all[client.id] = client
        return client
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * 
            FROM clients
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls,id):
        sql = """
            SELECT *
            FROM clients
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls,name):
        sql = """
            SELECT *
            FROM clients
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
