gender = input('How is your gender? [m, v] ')
age = int(input('How old are you? '))


if gender == 'm':
    if age < 21:
        print('boy')
    else:
        print('man')

elif gender == 'f':
    if age < 21:
        print('girl')
    else:
        print('woman')

else:
    print('other')
    

print('Done')

