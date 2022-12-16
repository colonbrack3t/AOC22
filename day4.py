rawdata = open("day4input","r").read()
data = rawdata.split('\n')
score = 0
for d in data:
    elf1,elf2 = d.split(',')
    min1,max1 = elf1.split('-')
    min2,max2 = elf2.split('-')
    min1 = int(min1)
    max1 = int(max1)
    min2 = int(min2)
    max2 = int(max2)
    if min1 <= min2 and max1>= max2:
        score+=1
        continue
    if min2 <= min1 and max2>= max1:
        score+=1


print('\033[91m' + str(score))
score = 0
for d in data:
    elf1,elf2 = d.split(',')
    min1,max1 = elf1.split('-')
    min2,max2 = elf2.split('-')
    min1 = int(min1)
    max1 = int(max1)
    min2 = int(min2)
    max2 = int(max2)
    id1 = range(min1,max1+1)
    id2 = range(min2,max2+1)
    if min1 in id2 or max1 in id2 or min2 in id1 or max2 in id1:
        score += 1


print('\033[91m' + str(score),'\033[0m')