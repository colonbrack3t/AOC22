rawdata = open("day6input","r").read()
data = rawdata.split('\n')


selection_size = 4
for i in range(len(rawdata)-selection_size-1):
    selection = list(rawdata[i:i+selection_size])
    if len(selection) == len(set(selection)):
        print('\033[91m' + ''.join(selection), i+selection_size)
        break

selection_size = 14
for i in range(len(rawdata)-selection_size-1):
    selection = list(rawdata[i:i+selection_size])
    if len(selection) == len(set(selection)):
        print('\033[91m' + ''.join(selection), i+selection_size,'\033[0m')
        break
