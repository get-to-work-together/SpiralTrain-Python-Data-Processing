# -*- coding: utf-8 -*-
"""
Created on Mon May 23 15:47:30 2022

@author: peter
"""

class BankAccount:

    def __init__(self, iban, name):
        self.__iban = iban
        self.__account_holder = name
        self.__balance = 0.0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)
    
    def info(self):
        print('Account %s of %s has a balance of €%.2f' % (self.__iban, 
                                                           self.__account_holder,
                                                           self.__balance))

    def __repr__(self):
        return f'BankAcount("{self.__iban}", "{self.__account_holder}")'
        
    def __str__(self):
        return f'BankAcount: nr.: {self.__iban} holder: {self.__account_holder} balance = {self.__balance}'
        
# --------------------------------------

if __name__ == '__main__':

    acc1 = BankAccount('NL86INGB0564654689', 'Peter')
    acc1.deposit(200)
    acc1.withdraw(50)
    
    acc2 = BankAccount('NL45ABCA0354253678', 'Stefanie')
    acc2.deposit(1000)
    acc2.withdraw(100)
    
    acc1.info()
    acc2.info()
    
    acc1.transfer(acc2, 88)

    acc1.info()
    acc2.info()
    
