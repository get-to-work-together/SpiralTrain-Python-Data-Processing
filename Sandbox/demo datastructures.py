
#%% Lists

numbers = [3,6,8,3,7,4,6]

print(type(numbers))
print(numbers)

words = 'the cat is stuck in the tree'.split()

print(words)

#%% Built-in functions

print('len',   len(numbers)  )
print('len',   len(words)  )

len('abcdefg')

print('sum',   sum(numbers)  )
print('min',   min(numbers)  )
print('max',   max(numbers)  )

print('min',   min(words)  )
print('max',   max(words)  )

print('sorted',   sorted(words)  )


#%% Indexing and slicing

print(words[0])
print(words[1])
print(words[-1])
print(words[-2])

print(words[1:4])
print(words[-3:])

#%% methods

print(words.count('the'))

print(words.index('the'))
print(words.index('the', 1))

#%% modification methods

words.append('last')
print(words)

words.insert(0, 'first')
print(words)

print(words.pop())
print(words)

print(words.pop(0))
print(words)

words.sort()
print(words)

words.sort(reverse = True)
print(words)

#%% Sets

s = set([1,1,1,2,3,6])

s.add(9)

s.remove(9)

s.discard(9)

#%% Dictionaries

d = {'nl':'+31', 'b':'+32', 'uk':'+44'}

d['nl']

d['f'] = '+39'

d['f'] = '+37'

del d['uk']

d.keys()
d.values()
d.items()

d_reversed = {v: k for k, v in d.items()}

d_reversed = dict(zip(d.values(), d.keys()))


