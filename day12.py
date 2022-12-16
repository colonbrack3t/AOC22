rawdata = open("day12input","r").read()
data = rawdata.split('\n')
start = ''
end = ''
distances = []
width = len(data[0])
height = len(data)
big = width*height*10#extra *10 to be safe but shbould be biger than any dist possible
numbered_data = []
values = 'zyxwvutsrqponmlkjihgfedcba'
unvisited = []

for i in range(width) :
    
    col = []
    number_col = []
    for j in range(height):
        unvisited.append((i,j))
        if data[j][i] == 'S':
            end = (i,j)
            number_col.append(len(values)-1)
            col.append(big)
        elif 'E' in data[j][i]:
            start = (i,j)
            number_col.append(0)
            col.append(0)

        else:
            number_col.append(values.index(data[j][i]))
            col.append(big)
    distances.append(col)
    numbered_data.append(number_col)


def Dijk(start,end, distances,unvisited,numbered_data):
    curr_node= start
    if start in unvisited:
        unvisited.pop(unvisited.index(start))
    while  len(unvisited)>0:
    

        x = curr_node[0]
        y = curr_node[1]
        v = numbered_data[x][y]
    
        #get neighbour options
        neighbours = []
        for i in range(-1,2,2):
            if  width > x + i >= 0 and numbered_data[x+i][y] - v <= 1:
                neighbours.append((x+i,y))
        for j in range(-1,2,2):
            if  height > y + j >= 0 and numbered_data[x][y+j] - v <= 1:
                neighbours.append((x,y+j))
        for n in neighbours:
            if n in unvisited:
                alt = distances[x][y] + 1
                if alt < distances[n[0]][n[1]] :
                    distances[n[0]][n[1]] = alt
        unvisited.sort(key = lambda t: distances[t[0]][t[1]])
        curr_node = unvisited.pop(0)

    return distances[end[0]][end[1]], distances
p1 , evaled_distances = Dijk(start,end,  [x[:] for x in distances], unvisited.copy(),numbered_data)

print(f'\033[91m{p1}')

a_vertices = [t for t in unvisited if numbered_data[t[0]][t[1]] == len(values)-1]
a_vertices.sort(key= lambda t:evaled_distances[t[0]][t[1]])
shortest = evaled_distances[a_vertices[0][0]][a_vertices[0][1]]
print(shortest,'\033[0m') 
