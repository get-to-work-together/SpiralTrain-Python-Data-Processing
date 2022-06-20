def maximum(*numbers):
    highest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
    return highest


def minmax1(*numbers):
    lowest = numbers[0]
    highest = numbers[0]

    for number in numbers[1:]:
        if number > highest:
            highest = number
        if number < lowest:
            lowest = number
            
    return lowest, highest


def minmax2(*numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[0], sorted_numbers[-1]




def f1(a, b, c, d=None, e=None, f=None):
    print(a, b, c, d, e, f)
    

def f2(*args, **kwargs):
    print(args, kwargs)
    print(kwargs.get('f'))
    f1(*args, **kwargs)


maximum(2, 5)
maximum(2, 5, 7, 3, 4)
