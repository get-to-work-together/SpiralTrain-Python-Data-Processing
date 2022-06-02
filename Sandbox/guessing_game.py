# -*- coding: utf-8 -*-
"""
Created on Tue May 24 10:15:04 2022

@author: peter
"""

import random

secret_number = random.randint(1, 100)

number_of_guesses = 0
while True:
    
    try:
        guess = int(input('What is you guess? '))
        
    except ValueError:
        print("Sorry. That's not a number.")  
        continue
    
    except KeyboardInterrupt:
        print('Thank you for playing. Goodbye.')
        break
    
    except:
        print('Oops. Some else went wrong.')
    
    number_of_guesses += 1
    
    if guess < secret_number:
        print('higher ...')
        
    elif guess > secret_number:
        print('lower ...')   
        
    else:
        print(f'YEAH!!! You guessed it in {number_of_guesses} times.')
        break
        