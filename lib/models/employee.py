# lib/models/employee.py
from models.__init__ import CURSOR, CONN

class Employee:
    # A dictionary that will save to the database
    all = {}

    #Initialization
    def __init__(self, name, duty_assigned, id= None):
        self.id = id
        self.name = name
        self.duty_assigned = duty_assigned

    def __repr__(self):
        return (
            f"<Employee {self.id}: {self.name}, {self.duty_assigned}"
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
        
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY,
            name TEXT,
            duty_assigned TEXT)
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
            INSERT INTO employees(name, duty_assigned) VALUES (?,?)
        """
        CURSOR.execute(sql, (self.name, self.duty_assigned))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, duty_assigned):
        employee = cls(name, duty_assigned)
        employee.save()
        return employee
    
    def update(self):
        sql = """
            UPDATE employees
            SET name = ?, duty_assigned = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.duty_assigned, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM employees
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()