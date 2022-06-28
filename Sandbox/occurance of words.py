s = r"""
Founded in the 1860’s, GustoMSC are experienced and reputable designers and engineers of mobile offshore units and equipment, with a long and rich history in the maritime industry.

In close cooperation with our clients, we translate experience, science, and technical knowledge into realistic and innovative ideas to solve customers’ unique challenges – an approach ingrained in our culture.

By our operational support and engineering consultancy, the performance of new and existing jack-ups, vessels, and semi-submersibles is further optimized.

GustoMSC enables and supports safe and efficient operations at sea."""


#%%

#s = s.lower().replace('.', '').replace(',', '').replace('(', '').replace(')', '').replace('–','').replace("’",'')

#s = s.lower().translate(str.maketrans('', '', '.,()[]-?!\’'))

import re
s = re.sub('^[a-z ]', '', s.lower())


#%%

words = s.split()

unique_words = set(words)

#%%

d = dict()
for word in unique_words:
    n = words.count(word)
    d[word] = n

#%%

for word, n in sorted(d.items(), key = lambda item: item[1], reverse = True):
    print(f'{word:20}: {n:3} {"*" * n}')
    


















#-------------------------------------------------

# import string

# clean up
# s = s.lower().replace('.', '').replace(',', '').replace('(', '').replace(')', '')
# or
# s = s.lower().translate(str.maketrans('', '', string.punctuation))
# or
# import re
# s = re.sub(r'[^a-zA-Z0-9 ]', '', s)

# words = s.split()

# unique_words = set(words)

# d = dict()
# for word in unique_words:
#     n = words.count(word)
#     d[word] = n

# or
# d = {word: words.count(word) for word in set(words)}

# for word, n in sorted(d.items(), key = lambda item: item[1], reverse=True):
#     print(f'{word:20}: {n:3} {"*" * n}')

# def get_values(item):
#     return item[1]
#
# for word, n in sorted(d.items(), key=get_values, reverse=True):
#     # print(word, n)
#     # print('%-25s: %3d' % (word, n))
#     print(f'{word:<25}: {n:3}')
#     # or
#     print('%-15s: %3d %s' % (word, n, '*' * n))
