# lib/models/employee.py
from models.__init__ import CURSOR, CONN
from models.hotel import Hotel

class Employee:
    # A dictionary that will save to the database
    all = {}

    #Initialization
    def __init__(self, name, duty_assigned, hotel_id, id= None):
        self.id = id
        self.name = name
        self.duty_assigned = duty_assigned
        self.hotel_id = hotel_id

    def __repr__(self):
        return (
            f"<Employee {self.id}: {self.name}, {self.duty_assigned}, " +
            f"Hotel ID: {self.hotel_id}>"
        )

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must not be an empty string")
        
    @property
    def duty_assigned(self):
        return self._duty_assigned
    @duty_assigned.setter
    def duty_assigned(self, duty_assigned):
        if isinstance(duty_assigned, str) and len(duty_assigned):
            self._duty_assigned = duty_assigned
        else:
            raise ValueError("Duty assigned must be a non-empty string")
        
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
            CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY,
            name TEXT,
            duty_assigned TEXT,
            hotel_id INTEGER,
            FOREIGN KEY(hotel_id) REFERENCES hotels(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS employees;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO employees(name, duty_assigned, hotel_id) VALUES (?,?,?)
        """
        CURSOR.execute(sql, (self.name, self.duty_assigned, self.hotel_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, duty_assigned, hotel_id):
        employee = cls(name, duty_assigned, hotel_id)
        employee.save()
        return employee
    
    def update(self):
        sql = """
            UPDATE employees
            SET name = ?, duty_assigned = ?, hotel_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.duty_assigned, self.hotel_id, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM employees
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None


    @classmethod
    def instance_from_db(cls, row):
        employee = cls.all.get(row[0])
        if employee:
            employee.name = row[1]
            employee.duty_assigned = row[2]
            employee.hotel_id = row[3]
        else:
            employee = cls(row[1],row[2],row[3])
            employee.id = row[0]
            cls.all[employee.id] = employee
        return employee
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * 
            FROM employees
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls,id):
        sql = """
            SELECT *
            FROM employees
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls,name):
        sql = """
            SELECT *
            FROM employees
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    

