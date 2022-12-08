rawdata = open("day3input","r").read()
data = rawdata.split('\n')
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
score = 0

for d in data:
    l = int(len(d)/2)
    half1 = d[:l]
    half2 = d[l:]
    for l in half1:
        if l in half2:
            score += 1 + chars.index(l)
            break
print('\033[91m' + str(score))
score = 0
for i in range(0,len(data),3):
    elf1 = data[i]
    elf2 = data[i+1]
    elf3 = data[i+2]
    found = False
    for l in elf1:
        if l in elf2 and l in elf3:
            score += 1 + chars.index(l)
            found = True
            break
    if not found:
        print('ERROR')#just to ensure we definietle get em all 
print('\033[91m' + str(score),'\033[0m')