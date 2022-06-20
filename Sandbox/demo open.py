
filename = 'text.txt'


#%%

f = open(filename, 'r')
content = f.read()
f.close()


#%%

with open(filename, 'r') as f:
    content = f.read()

print(content)



#%%
with open(filename, 'r') as f:
    print('line 1:',  f.readline().rstrip())
    print('line 2:',  f.readline().rstrip())
    print('line 3:',  f.readline().rstrip())


#%%
with open(filename, 'r') as f:
    for linenr, line in enumerate(f, start = 1):
        print(f'line {linenr}:',  line.rstrip())


        
#%%
with open(filename, 'r') as f:
    for linenr, line in enumerate(f, start = 1):
        if 'line' in line.lower():
            print(f'line {linenr}:',  line.rstrip())
            

#%%
with open(filename, 'r') as f:
    for linenr, line in enumerate(f, start = 1):
        words = line.rstrip().split()
        if len(list(filter(lambda w: w.startswith('r'), words)))>0:
            print(f'line {linenr}:',  line)


#%%
import re
with open(filename, 'r') as f:
    for linenr, line in enumerate(f, start = 1):
        if re.search(r'\br\w*', line.rstrip()):
            print(f'line {linenr}:',  line)






