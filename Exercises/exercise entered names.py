names = []

while True:
    
    new_name = input('Enter a name: ')
    
    if new_name:
        names.append(new_name)
    
    else:
        break


print('\nThe names you entered were:')

for name in sorted(names):
    print(name)
