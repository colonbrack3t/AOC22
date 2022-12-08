import re
rawdata = open("day2input","r").read()
data = rawdata.split('\n')
score= 0
for d in data:
    op , me = d.split(' ')
    if me == 'X':
        score += 1
        if op == 'A':
            score += 3
        if op == 'B':
            score += 0
        if op == 'C':
            score += 6
    if me == 'Y':
        score += 2
        if op == 'A':
            score += 6
        if op == 'B':
            score += 3
        if op == 'C':
            score += 0
    if me == 'Z':
        score += 3
        if op == 'A':
            score += 0
        if op == 'B':
            score += 6
        if op == 'C':
            score += 3
print('\033[91m' + str(score))
score= 0
for d in data:
    op , me = d.split(' ')
    if me == 'X':
        score += 0
        if op == 'A':
            score += 3
        if op == 'B':
            score += 1
        if op == 'C':
            score += 2
    if me == 'Y':
        score += 3
        if op == 'A':
            score += 1
        if op == 'B':
            score += 2
        if op == 'C':
            score += 3
    if me == 'Z':
        score += 6
        if op == 'A':
            score += 2
        if op == 'B':
            score += 3
        if op == 'C':
            score += 1
print('\033[91m' + str(score),'\033[0m')