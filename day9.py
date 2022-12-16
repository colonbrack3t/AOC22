rawdata = open("day9input","r").read()
data = rawdata.split('\n')
head_pos = [0,0]
tail_pos = [0,0]

visited_tail_pos = [(0,0)]

visited_1_pos = [(0,0)]

min_dist = pow(2,0.5)

def get_vector_between(head,tail):
    diff1 = head[0]-tail[0]
    diff2 = head[1]-tail[1]
    return [diff1,diff2]
def mag(vector):
    return pow( ( (vector[0]**2) + (vector[1]**2) )  ,0.5)

def distance(head,tail):
    return mag(get_vector_between(head,tail))

#red print
def pretty_print_rope(rope,l=10,w=10):
    for y in range(l,-l,-1):
        row = ''
        for x in range(-w,w):
                char = '.'
                for n , r in enumerate(rope):
                    i , j = r
                    if x == i and y == j:
                        char = str(n)
                        
                row += char
        print(row)
                   
rope = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
#pretty_print_rope(rope)
for d in data:
    direction,magnitude = d.split(' ')
    magnitude = int(magnitude)

    for i in range(magnitude):
        if direction == 'R':
            rope[0][0]+=1
        elif direction == 'L':
            rope[0][0] -=1
        elif direction == 'U':
            rope[0][1]+=1
        elif direction == 'D':
            rope[0][1]-=1
        for r in range(1,10):
            if distance(rope[r-1],rope[r]) > min_dist:
                # move tail
                v = get_vector_between(rope[r-1],rope[r])
                if abs(v[0]) >= 2:
                    if abs(v[1]) >=1 :
                        #move diag
                        rope[r][0]+= 1 if v[0] > 0 else -1
                        rope[r][1]+= 1 if v[1] > 0 else -1
                    else:
                        #move straight line
                        rope[r][0]+= 1 if v[0] > 0 else -1
                elif abs(v[1])>=2:
                    if abs(v[0]) >=1 :
                        #move diag
                        rope[r][0]+= 1 if v[0] > 0 else -1
                        rope[r][1]+= 1 if v[1] > 0 else -1
                    else:
                        #move straight line
                        rope[r][1]+= 1 if v[1] > 0 else -1
        #pretty_print_rope(rope)
        visited_tail_pos.append(tuple(rope[9]))
        visited_1_pos.append(tuple(rope[1]))

print(f'\033[91m{len(set(visited_1_pos))}') 
print(len(set(visited_tail_pos)),'\033[0m')