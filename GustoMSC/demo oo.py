# -*- coding: utf-8 -*-
"""
Created on Mon May 23 15:13:23 2022

@author: peter
"""

from person import Person
from bankaccount import BankAccount
from my_functions import say_goodmorning
        
#---------------------------------------------------------------------

p = Person('Peter', 'Lhee')

print(p.tell())
    
say_goodmorning()

acc1 = BankAccount('NL23ABCD098767889', 'Peter')
acc1.deposit(1000)
acc1.withdraw(200)
print(acc1.info())