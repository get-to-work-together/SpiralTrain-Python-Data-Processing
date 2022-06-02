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

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        self.__balance = amount
        
    @staticmethod
    def add_numbers(*numbers):
        return sum(numbers)

    @staticmethod
    def build_account1(amount):
        acc = BankAccount('00', 'Unknown')
        acc.balance = amount
        return acc
    
    @classmethod
    def build_account2(cls, amount):
        acc = cls('00', 'Unknown')
        acc.balance = amount
        return acc
    
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
    
    print( acc1.balance )
    
    acc1.balance = 1000000
    print( acc1.balance )
    
    acc3 = BankAccount.build_account(500)
    print( acc3 )
    