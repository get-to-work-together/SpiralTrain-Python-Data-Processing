
while True:
    number = int(input('Enter an number between 1 and 10: '))

    if 1 <= number <= 10:
        break


while True:
    gender = input('What is your gender? [m,f]: ')

    if gender in ('m','f'):
        break


print(f'The number is {number}')
print(f'Your gender is {gender}')
