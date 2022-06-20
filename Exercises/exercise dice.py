import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
dice3 = random.randint(1, 6)
dice4 = random.randint(1, 6)
dice5 = random.randint(1, 6)

total = dice1 + dice2 + dice3 + dice4 + dice5

print('Dice:', dice1, dice2, dice3, dice4, dice5)
print('Total:', total)

#---------------------------------

total = 0
for i in range(5):
    total += random.randint(1, 6)

print('Total:', total)

#---------------------------------

dice = []
for i in range(5):
    dice.append( random.randint(1, 6) )
total = sum(dice)

print('Dice:', dice)
print('Total:', total)

#---------------------------------

dice = [random.randint(1, 6) for _ in range(5)]   # comprehension
total = sum(dice)

print('Dice:', dice)
print('Total:', total)
