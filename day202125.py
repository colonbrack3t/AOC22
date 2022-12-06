rawdata = open("dayinput","r").read()
data = rawdata.split('\n')
next_state = []
for j in range(len(data)):
    next_state_row = []
    for i in range(len(data[0])):
        space = data[j][i]
        if space is '.':
            continue
        elif space is '>':
            next_space = data[j][(i + 1) % len(data[0])]
            if next_space is '.':
                pass
