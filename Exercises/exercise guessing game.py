import random

secret_number = random.randint(1, 100)

print('Guess a number between 1 and 100')

number_of_guesses = 0
while True:

    try:
        guess = int(input('What is your guess? '))
        
    except ValueError:   
        print('That number is not a number')
        continue
    
    number_of_guesses += 1
    
    if not 1 <= guess <= 100:
        print('That number is not between 1 and 100')
    
    elif guess < secret_number:
        print('higher ...')
        
    elif guess > secret_number:
        print('lower ...')
        
    else:
        print(f'Yeaah! The number was indeed {secret_number}')
        print(f'You guessed it in {number_of_guesses} guesses.')
        break


#%% EAFP

secret_number = random.randint(1, 100)

print('Guess a number between 1 and 100')

number_of_guesses = 0
while True:

    try:
        guess = int(input('What is your guess? '))
    except:
        print('That\'s not a number.')
        continue
    number_of_guesses += 1
    
    if guess < secret_number:
        print('higher ...')
        
    elif guess > secret_number:
        print('lower ...')
        
    else:
        print(f'Yeaah! The number was indeed {secret_number}')
        print(f'You guessed it in {number_of_guesses} guesses.')
        break


#%% LBYL

secret_number = random.randint(1, 100)

print('Guess a number between 1 and 100')

number_of_guesses = 0
while True:

    user_input = input('What is you guess? ')
    if user_input.isdecimal():
        guess = int(user_input)
    else:
        print('That\'s not a number.')
        continue
    
    number_of_guesses += 1
    
    if guess < secret_number:
        print('higher ...')
        
    elif guess > secret_number:
        print('lower ...')
        
    else:
        print(f'Yeaah! The number was indeed {secret_number}')
        print(f'You guessed it in {number_of_guesses} guesses.')
        break

#%% or

secret_number = random.randint(1, 100)

print('Guess a number between 1 and 100')

n = 0
while True:
    # Throwing an exception
    try:
        user_input = input('What is you guess? ')
        if user_input.isdecimal():
            guess = int(user_input)
        else:
            raise Exception('That\'s not a number.')
            
    except Exception as ex:
        print('Error: ', ex)
        continue

    n += 1
    
    if guess < secret_number:
        print('higher ...')
        
    elif guess > secret_number:
        print('lower ...')
        
    else:
        print(f'Yeaah! The number was indeed {secret_number}')
        print(f'You guessed it in {n} guesses.')
        break
    

#%% or

class MyOwnException(Exception):
    pass


secret_number = random.randint(1, 100)

print('Guess a number between 1 and 100')

n = 0
while True:
    # Throwing an exception
    try:
        user_input = input('What is you guess? ')
        if user_input.isdecimal():
            guess = int(user_input)
        else:
            raise MyOwnException('That\'s not a number.''')
            
    except MyOwnException as ex:
        print('Error: ', ex)
        continue

    n += 1
    
    if guess < secret_number:
        print('higher ...')
        
    elif guess > secret_number:
        print('lower ...')
        
    else:
        print(f'Yeaah! The number was indeed {secret_number}')
        print(f'You guessed it in {n} guesses.')
        break