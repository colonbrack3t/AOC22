data = open("day1input","r").read().split('\n')
calories = []
running_total = 0
for d in data:
    if d == '':
        calories.append(running_total)
        running_total = 0
    else:
        running_total+=int(d)
calories.sort()
print(calories[-1])
print( sum(calories[-3:]))