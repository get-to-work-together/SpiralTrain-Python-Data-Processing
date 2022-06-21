
year = int(input('Which year? '))

is_leapyear = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

if is_leapyear:
    print(year, 'is a leapyear')
else:
    print(year, 'is NOT a leapyear')


#%% or

dividable_by_4 = year % 4 == 0
dividable_by_100 = year % 100 == 0
dividable_by_400 = year % 400 == 0

is_leapyear = dividable_by_4 and not dividable_by_100 or dividable_by_400

if is_leapyear:
    print(f'{year} is a leapyear')
else:
    print(f'{year} is NOT a leapyear')
