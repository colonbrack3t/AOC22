rawdata = open("day8input","r").read()
data = rawdata.split('\n')
visible_trees = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        
        tree = data[i][j]
        visible = True
        for above in range(i):
            visible &= data[above][j] < tree
        if visible:
            visible_trees +=1
            continue
        visible = True
        for below in range(i+1, len(data)):
            visible &= data[below][j] < tree
        if visible:
            visible_trees +=1
            continue
        visible = True
        for right in range(j):
            visible &= data[i][right] < tree
        if visible:
            visible_trees +=1
            continue
        visible = True
        for left in range(j+1, len(data[i])):
            visible &= data[i][left] < tree
        if visible:
            visible_trees +=1
            continue
        visible = True
max_viewing_distance = 0
for i in range(len(data)):
    for j in range(len(data[i])):

        tree = data[i][j]
        a = 0
        for above in range(i-1,-1,-1):

            a+=1
            if data[above][j] >= tree:
                break
        b = 0
        for below in range(i+1, len(data)):
            b+=1
            if data[below][j] >= tree:
                break
        r = 0
        for right in range(j-1,-1,-1):
            r+=1
            if data[i][right] >= tree:
                break
        l = 0
        for left in range(j+1, len(data[i])):
            l+=1
            if data[i][left] >= tree:
                break
        scenic_distance = a * b * l * r

        if max_viewing_distance < scenic_distance:

            max_viewing_distance = scenic_distance

print(f'\033[91m{visible_trees}') #red print
print(f'{max_viewing_distance}\033[0m') #red print
