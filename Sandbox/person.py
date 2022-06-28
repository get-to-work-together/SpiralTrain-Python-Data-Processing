# -*- coding: utf-8 -*-
"""
Created on Mon May 23 15:34:35 2022

@author: peter
"""


#%%

class Person:

    def __init__(self, name, residence = 'unknown', height = 0):
        self.name = name
        self.residence = residence
        self.height = height

    def tell(self):
        return(f'I am {self.name} and I live in {self.residence}')

    def move(self, new_residence):
        self.residence = new_residence
        
    def __str__(self):
        return f'Person with name {self.name}'

    def __repr__(self):
        return f"Person('{self.name}', '{self.residence}')"
    
    def __len__(self):
        return self.height
    
    def __add__(self, other):
        return self.height + other.height
        

        
p1 = Person('Steven', 'Spijkenisse', 190)
p2 = Person('Anand', 'Delft', 186)

print( p1.tell() )
print( p2.tell() )

print( Person.tell(p1) )

p2.move('Schiedam')

print( p1.tell() )
print( p2.tell() )
















#%%

# class Person:
#     """This is my great Person class"""
    
#     __slots__ = ['_name', '_residence', '_bankaccounts']
    
#     def __init__(self, name, residence):
#         self._name = name
#         self._residence = residence
#         self._bankaccounts = []
        
#     @property
#     def residence(self):
#         return self._residence.upper()
    
#     @residence.setter
#     def residence(self, value):
#         if value:
#             self._residence = value
#         else:
#             raise Exception('Can not specify an empty residence.')

#     @property
#     def name(self):
#         return self._name
    
#     def __repr__(self):
#         return f"Person('{self._name}', '{self._residence}')"
    
#     def __str__(self):
#         return f'Person: name: {self._name}, residence: {self._residence}'
        
#     def tell(self):
#         """This method returns the residence of the target object"""
#         return f'I am {self._name} and I live in {self._residence}.'
    
#     def move(self, new_residence):
#         """This method changes the residence attribute of the target object"""
#         self._residence = new_residence
    
        
  #%%      
        

class Notes:
    def __init__(self):
        self._notes = []
    def log(self, note):
        self._notes.append(note)


#%%

class Employee(Person, Notes):   
    
    __slots__ = ['_employee_nr']
        
    def __init__(self, name, residence, employee_nr):
        super().__init__(name, residence)
        Notes.__init__()
        self._employee_nr = employee_nr
        
    def __repr__(self):
        return f"Employee('{self._name}', '{self._residence}', '{self._employee_nr}')"
    
    def tell(self):
        """This method returns the residence of the target object"""
        return f'I am {self._name} and my employee number is {self._employee_nr}.'
    
#%%    
# ------------------------------------------------------------------------        

if __name__ == '__main__':     
    
    p = Person('Jan', 'Amsterdam')
    print(p.tell())
     
    employees = []
    employees.append( Employee('Peter', 'Lhee', 'guest'))
    employees.append( Employee('Tobias', 'Voorschoten', '4769823'))
    
    for employee in employees:
        print(employee.tell())
    
    
    