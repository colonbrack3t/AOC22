import re
numbers = ' ([0-9]+)'
rawdata = open("day5input","r").read()
data = rawdata.split('\n')
start_reading_move_inputs_from = 0
def get_stacks():
    global start_reading_move_inputs_from
    stacks = ''
    for i in range(len(data)):
        d = data[i]
        if d == '':
            start_reading_move_inputs_from = i
            return stacks
        else:
            stacks += d + '\n' 

stacks = get_stacks()

stacks = stacks.split('\n')
piles = {i+1 : [] for i in range(9)}
for stack in stacks[:-2]:
    for i in range(0,len(stack),4):
        l = stack[i+1]
        if l != ' ':
            piles[int(i/4)+1].append(l)
for d in data[start_reading_move_inputs_from+1:]:
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


stacks = get_stacks()
stacks = stacks.split('\n')
piles = {i+1 : [] for i in range(9)}
for stack in stacks[:-2]:
    for i in range(0,len(stack),4):
        l = stack[i+1]
        if l != ' ':
            piles[int(i/4)+1].append(l)
for d in data[start_reading_move_inputs_from+1:]:
    n , from_i , to_i = map(int, re.findall(numbers,d))

    items = piles[from_i][:n]
    piles[from_i] = piles[from_i][n:]
    items.extend(piles[to_i])
    piles[to_i] = items
    

    
w=''
for p in piles.items():
    w += p[1][0]
print('\033[91m' + str(w),'\033[0m')
