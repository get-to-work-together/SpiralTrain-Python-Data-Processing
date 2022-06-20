import random

secret_number = random.randint(1, 100)

print('Guess a number between 1 and 100')


class MyOwnException(Exception):
    pass


n = 0
while True:

    # LBYL
    # user_input = input('What is you guess? ')
    # if user_input.isdecimal():
    #     guess = int(user_input)
    # else:
    #     print('That\'s not a number.')
    #     continue

    # EAFP
    # try:
    #     guess = int(input('What is you guess? '))
    # except:
    #     print('That\'s not a number.')
    #     continue

    # Throwing an exception
    try:
        user_input = input('What is you guess? ')
        if user_input.isdecimal():
            guess = int(user_input)
        else:
            raise MyOwnException('That\'s not a number.''')
    except MyOwnException:
        print('Got yea')

    
    n += 1
    
    if guess < secret_number:
        print('higher ...')
        
    elif guess > secret_number:
        print('lower ...')
        
    else:
        print(f'Yeaah! The number was indeed {secret_number}')
        print(f'You guessed it in {n} guesses.')
        break