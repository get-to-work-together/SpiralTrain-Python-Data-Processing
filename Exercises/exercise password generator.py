#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:25:05 2022

@author: peter
"""

import random

def password_generator(required_length = 8,
                       n_lowercase = 2,
                       n_uppercase = 2,
                       n_numbers = 1,
                       n_special = 1):

    lowercase_characters = 'abcdefghijkmnopqrstuvwxyz' # removed l
    uppercase_characters = 'ABCDEFGHJKLMNPQRSTUVWXYZ' # removed I and O
    number_characters = '0123456789'
    special_characters = '@#$%&*+?!'
    
    lower = random.choices(lowercase_characters, k = n_lowercase)
    upper = random.choices(uppercase_characters, k = n_uppercase)
    numbers = random.choices(number_characters, k = n_numbers)
    special = random.choices(special_characters, k = n_special)
    
    extra = random.choices(lowercase_characters +
                           uppercase_characters +
                           number_characters +
                           special_characters,
                           k = required_length - n_lowercase - n_uppercase - n_numbers - n_special)
    
    all = lower + upper + numbers + special + extra
    
    random.shuffle(all)
    
    return ''.join(all)

#------------------------------------------------------------------

password = password_generator()
print('New password: ', password)


#%%

def password_generator(required_length = 8,
                       n_lowercase = 2,
                       n_uppercase = 2,
                       n_numbers = 1,
                       n_special = 1):

    character_groups = (
        (n_lowercase, 'abcdefghijkmnopqrstuvwxyz'), # removed l
        (n_uppercase, 'ABCDEFGHJKLMNPQRSTUVWXYZ'), # removed I and O
        (n_numbers,   '0123456789'),
        (n_special,   '@#$%&*+?!')
    )
      
    all_characters = ''
    characters = []
    for n, character_group in character_groups:
        all_characters += character_group
        characters.extend(random.choices(character_group, k = n))
        
    characters.extend(random.choices(all_characters, 
                                     k = required_length - len(characters)))
        
    random.shuffle(characters)
    
    return ''.join(characters)

#------------------------------------------------------------------

password = password_generator()
print('New password: ', password)