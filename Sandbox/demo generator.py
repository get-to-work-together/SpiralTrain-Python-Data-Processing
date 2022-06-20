
#%%

def count(n):
    numbers = []
    for i in range(1, n+1):
        numbers.append(i)
    return numbers


#%%

def count_yield(n):
    for i in range(1, n+1):
        yield i


#%%

g = (x**2 for x in range(20))



#%%

if __name__ == '__main__':
    
    for number in count_yield(300):
        print(number)