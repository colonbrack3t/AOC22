rawdata = open("day10input","r").read()
data = rawdata.split('\n')
cycle = 0 
X = 1
signal_strengths = []
screen = ''

def check_cycle(cycle):
    if cycle > 0 and  (cycle - 20) % 40 == 0:
        global signal_strengths
        signal_strengths.append(X*cycle)

def render_pixel(cycle,X):
    global screen
    if cycle % 40 == 0 and not screen== '':
        screen+='\n'
    #symbols changed to % and ' ' for improved legibility
    if X == (cycle % 40) or X == (cycle % 40)-1 or X == (cycle % 40) +1:
        screen+='#'
    else:
        screen +=' '

def do_cycle():
    global cycle

    render_pixel(cycle,X)
    cycle+=1
    check_cycle(cycle)

for d in data:
    cmd = d.split(' ')
    if cmd[0] == 'noop':
        do_cycle()
    else:
        do_cycle()
        do_cycle()
        X += int(cmd[1])


print(f'\033[91m{sum(signal_strengths[:6])}')
print('\033[1m' + screen,'\033[0m') #red print
