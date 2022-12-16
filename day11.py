rawdata = open("day11input","r").read()

class Monkey:
    items = []
    inspect = None
    operation = None
    num_inspects = 0
    def __init__(self, starting_items, operation, test_divisible, if_true, if_false):
        self.items = starting_items
        self.operation_strings = operation
        self.operation = self.operation_creation()
        self.inspect = lambda x: if_true if x % test_divisible == 0 else if_false

    def operation_creation(self):
        op = None
        if self.operation_strings[1] == '*':
            op = lambda x : (x if self.operation_strings[0] == 'old' else int(self.operation_strings[0])) * (x if self.operation_strings[2] == 'old' else int(self.operation_strings[2]))
        elif self.operation_strings[1] == '+':
            op = lambda x : (x if self.operation_strings[0] == 'old' else int(self.operation_strings[0])) + (x if self.operation_strings[2] == 'old' else int(self.operation_strings[2]))
        return op
omni_modulo = 1
monkeys = []
monkeys_starting_items = []
data = rawdata.split('\n')
for i in range(0,len(data),7):
    #starting items 
    starting_items = list(map(int,data[i+1].split(':')[1].replace(' ','').split(',')))
    operation_strings = data[i+2].split('=')[1][1:].split(' ')
    test_divisible = int(data[i+3].split('y')[1])
    omni_modulo*=test_divisible
    if_true = int(data[i+4].split('y')[1])
    if_false = int(data[i+5].split('y')[1])
    m = Monkey(starting_items,operation_strings,test_divisible,if_true,if_false)
    monkeys.append(m)
    monkeys_starting_items.append(starting_items.copy())

for rnd in range(20):
    for monkey in monkeys:
        while(len(monkey.items)>0):
            item = monkey.items.pop(0)
            
            item = int(monkey.operation(item)/3)
        

            monkeys[monkey.inspect(item)].items.append(item)
            monkey.num_inspects+=1
monkeys_sorted = monkeys.copy()
monkeys_sorted.sort(key = lambda m : m.num_inspects,reverse=True)
print(f'\033[91m{monkeys_sorted[0].num_inspects*monkeys_sorted[1].num_inspects}','\033[0m') #red print
#reset items
for i in range(len(monkeys)):
    monkeys[i].items = monkeys_starting_items[i]
    monkeys[i].num_inspects = 0
 

for rnd in range(10000):
    for monkey in monkeys:
        while(len(monkey.items)>0):
            item = monkey.items.pop(0)
            item = monkey.operation(item)
            item%=omni_modulo
            monkeys[monkey.inspect(item)].items.append(item)
            monkey.num_inspects+=1

monkeys.sort(key = lambda m : m.num_inspects,reverse=True)

print(f'\033[91m{monkeys[0].num_inspects*monkeys[1].num_inspects}','\033[0m') #red print
