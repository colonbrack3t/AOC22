rawdata = open("day14input","r").read()
data = rawdata.split('\n')
rock_map = {500:{0:'source'}}
biggest_x = 500
biggest_y = 0
smallest_x = 500
smallest_y = 0
def add_to_rock_map(p, value = 'rock', set_boundaries = True):
    if set_boundaries:
        global biggest_x, biggest_y, smallest_x, smallest_y, rock_map
        biggest_y = max(p[1],biggest_y)
        biggest_x = max(p[0],biggest_x)
        smallest_x = min(p[0],smallest_x)
        smallest_y = min(p[1],smallest_y)
    if p[0] in rock_map:
        rock_map[p[0]][p[1]] = value
    else:
        rock_map[p[0]] = {p[1] : value}

for d in data:
    points = list(map(lambda p: tuple(map(int,p.split(','))),d.split('->')))
    add_to_rock_map(points[0])
    for i in range(1, len(points)):
        from_p = points[i-1]
        to_p = points[i]
        if from_p[0] != to_p[0]:
            x_direction = 1 if to_p[0] - from_p[0] >= 0 else -1
            for x in range(from_p[0]+x_direction,to_p[0]+x_direction,x_direction):
                add_to_rock_map((x,from_p[1]))
        else: 
            y_direction = 1 if to_p[1] - from_p[1] >= 0 else -1
            for y in range(from_p[1]+y_direction,to_p[1]+y_direction,y_direction):
                add_to_rock_map((from_p[0],y))
def print_map(stone= (0,0)):
    global biggest_x, biggest_y, smallest_x, smallest_y, rock_map
    for y in range(smallest_y-1, biggest_y+3):
        output = ''
        for x in range(smallest_x, biggest_x+1):
            if x == stone[0] and y == stone[1]:
                output += 'o'
            elif x in rock_map and y in rock_map[x]:
                if rock_map[x][y] == 'rock':
                    output+='#'
                    continue
                elif rock_map[x][y] == 'stone':
                    output += 'o'
                    continue
                elif rock_map[x][y] == 'air':
                    output += '.'
                else:
                    output+='+'
            else:
                output += '.'
        print(output)

not_falling = True
stones = -1
while(not_falling):
    stones+=1
    moving = True
    stone = (500,0)
    
    while(moving):
       
        x,y = stone
        y+=1
        new_stone = (x,y)
        if x in rock_map and y in rock_map[x] and (rock_map[x][y] == 'rock' or rock_map[x][y] == 'stone'):
            #check diag left
            if x-1 in rock_map and y in rock_map[x-1] and (rock_map[x-1][y] == 'rock' or rock_map[x-1][y] == 'stone'):
                
                if x+1 in rock_map and y in rock_map[x+1] and (rock_map[x+1][y] == 'rock' or rock_map[x+1][y] == 'stone'):
                    add_to_rock_map(stone,'stone',False)
                    moving = False
                else:
                    
                    stone = (x+1,y)
            else:
                
                stone = (x-1,y)
                
        else:
            #still falling
            stone = new_stone
        if stone[1] >= biggest_y:
            not_falling = False
            break
print(f'\033[91m{stones}')
rock_map = {k : {i:j for i,j in v.items() if j != 'stone'} for k,v in rock_map.items()}


source_blocked = False
stones = -1

while(not source_blocked):
    stones+=1
    moving = True
    stone = (500,0)
    source_blocked = rock_map[500][0]!='source'
    while(moving):
       
        x,y = stone
        y+=1
        new_stone = (x,y)
        if y == biggest_y+2:
            add_to_rock_map(stone,'stone', False)
            moving = False
        if x in rock_map and y in rock_map[x] and (rock_map[x][y] == 'rock' or rock_map[x][y] == 'stone'):
            #check diag left
            if x-1 in rock_map and y in rock_map[x-1] and (rock_map[x-1][y] == 'rock' or rock_map[x-1][y] == 'stone'):
                
                if x+1 in rock_map and y in rock_map[x+1] and (rock_map[x+1][y] == 'rock' or rock_map[x+1][y] == 'stone'):
                    add_to_rock_map(stone,'stone',False)
                    moving = False
                else:
                    
                    stone = (x+1,y)
            else:
                
                stone = (x-1,y)
                
        else:
            #still falling
            stone = new_stone

print(stones,'\033[0m')
