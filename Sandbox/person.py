# -*- coding: utf-8 -*-
"""
Created on Mon May 23 15:34:35 2022

@author: peter
"""

class Person:
    """This is my great Person class"""
    
    def __init__(self, name, residence):
        self._name = name
        self._residence = residence
        self._bankaccounts = []
        
    def tell(self):
        """This method returns the residence of the target object"""
        return f'I am {self._name} and I live in {self._residence}.'
    
    def move(self, new_residence):
        """This method changes the residence attribute of the target object"""
        self._residence = new_residence
        
        
class Employee (Person):       
        
    def __init__(self, name, residence, employee_nr):
        super().__init__(name, residence)
        self._employee_nr = employee_nr
        
    def tell(self):
        """This method returns the residence of the target object"""
        return f'I am {self._name} and my employee number is {self._employee_nr}.'
        
# ------------------------------------------------------------------------        

if __name__ == '__main__':     
    
    p = Person('Jan', 'Amsterdam')
    print(p.tell())
     
    employees = []
    employees.append( Employee('Peter', 'Lhee', 'guest'))
    employees.append( Employee('Tobias', 'Voorschoten', '4769823'))
    
    for employee in employees:
        print(employee.tell())
    
    
    