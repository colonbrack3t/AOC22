rawdata = open("day13input","r").read()
data = rawdata.split('\n')
import json, functools
total = 0

def deep_list_comp(l1,l2):
    while(True):
        try:
            return 1 if l1 < l2 else -1 if l2 < l1 else 0       
        except Exception:
            def find_error(d1,d2,depth = 0):
                next_places = []
                for j , (v1 , v2) in enumerate(zip(d1,d2)):
                    if type(v1) == list and type(v2) == int:
                        d2[j] = [d2[j]]
                        
                    elif type(v2) == list and type(v1) == int:
                        d1[j] = [d1[j]]
                        
                    elif type(v1) == list and type(v2) == list:
                        next_places.append(j)
                for n in next_places:
                    d =  find_error(d1[n],d2[n])
                    if d !=  -1:
                        return
                return -1
            find_error(l1,l2)


for i in range(0,len(data),3):
 
    l1 = json.loads(data[i])
    l2 = json.loads(data[i+1])
    if (deep_list_comp(l1,l2)==1):
        total +=int(i/3)+1
print(f'\033[91m{total}')
divider_1 = '[[2]]'
divider_2 = '[[6]]'
data.append(divider_1)
data.append(divider_2)
def compare(l1,l2):
    l1 = json.loads(l1)
    l2 = json.loads(l2)
    return deep_list_comp(l1,l2)
data = [d for d in data if d != '']
data.sort(key=functools.cmp_to_key(compare), reverse=True)
print((data.index(divider_2)+1)*(1+data.index(divider_1)),'\033[0m') #red print
