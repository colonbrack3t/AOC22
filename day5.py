import re
numbers = ' ([0-9]+)'
rawdata = open("day5input","r").read()
data = rawdata.split('\n')

stacks = '''
[N]     [Q]         [N]            
[R]     [F] [Q]     [G] [M]        
[J]     [Z] [T]     [R] [H] [J]    
[T] [H] [G] [R]     [B] [N] [T]    
[Z] [J] [J] [G] [F] [Z] [S] [M]    
[B] [N] [N] [N] [Q] [W] [L] [Q] [S]
[D] [S] [R] [V] [T] [C] [C] [N] [G]
[F] [R] [C] [F] [L] [Q] [F] [D] [P]
 1   2   3   4   5   6   7   8   9 
'''
stacks = stacks.split('\n')
piles = {i+1 : [] for i in range(9)}
for stack in stacks[:-2]:
    for i in range(0,len(stack),4):
        l = stack[i+1]
        if l != ' ':
            piles[int(i/4)+1].append(l)
for d in data:
    n , from_i , to_i = map(int, re.findall(numbers,d))

    items = piles[from_i][:n]
    piles[from_i] = piles[from_i][n:]
    items.reverse()
    items.extend(piles[to_i])
    piles[to_i] = items
    

    
w=''
for p in piles.items():
    w += p[1][0]
print('\033[91m' + str(w))


stacks = '''
[N]     [Q]         [N]            
[R]     [F] [Q]     [G] [M]        
[J]     [Z] [T]     [R] [H] [J]    
[T] [H] [G] [R]     [B] [N] [T]    
[Z] [J] [J] [G] [F] [Z] [S] [M]    
[B] [N] [N] [N] [Q] [W] [L] [Q] [S]
[D] [S] [R] [V] [T] [C] [C] [N] [G]
[F] [R] [C] [F] [L] [Q] [F] [D] [P]
 1   2   3   4   5   6   7   8   9 
'''
stacks = stacks.split('\n')
piles = {i+1 : [] for i in range(9)}
for stack in stacks[:-2]:
    for i in range(0,len(stack),4):
        l = stack[i+1]
        if l != ' ':
            piles[int(i/4)+1].append(l)
for d in data:
    n , from_i , to_i = map(int, re.findall(numbers,d))

    items = piles[from_i][:n]
    piles[from_i] = piles[from_i][n:]
    items.extend(piles[to_i])
    piles[to_i] = items
    

    
w=''
for p in piles.items():
    w += p[1][0]
print('\033[91m' + str(w))
