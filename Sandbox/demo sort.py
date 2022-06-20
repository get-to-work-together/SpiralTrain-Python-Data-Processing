import random

numbers = [random.randint(-100, 100) for _ in range(20)]

print(numbers)

print(sorted(numbers))

print(sorted(numbers, reverse = True))

print(sorted(numbers, key = abs))

def distance_to_50(n):
    return abs(n - 50)

print(sorted(numbers, key = distance_to_50))


print(sorted(numbers, key = lambda n: abs(n - 30)))

def distance_to(n, center):
    return abs(n - center)

print(sorted(numbers, key = lambda n: distance_to(n, 30)))

print(list(map(lambda n: abs(n) * 100, numbers)))

print([abs(n) * 100 for n in numbers])

print(list(filter(lambda n: abs(n) > 70, numbers)))

print([n for n in numbers if abs(n) > 70])
