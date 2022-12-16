rawdata = open("day16input","r").read()
data = rawdata.split('\n')
import random
cave_system = {

}
biggest_tunnel_exit = 0
for d in data:
    valves_string, tunnels_string = d.split(';')
    valve_name = valves_string.split(' has')[0][6:]
    flow_rate = int(valves_string.split('=')[1])

    tunnel_exits = tunnels_string.split('valve')[1].replace('s','').replace(' ','').split(',')
    biggest_tunnel_exit = max(biggest_tunnel_exit,len(tunnel_exits))
    cave_system[valve_name] = {'flow_rate':flow_rate, 'exits':tunnel_exits, 'valve_closed':True}



def create_population(population_size):
    individuals = []
    for i in range(population_size):
        ind = []
        for t in range(30):
            open_or_close = random.randrange(0,2) == 0
            which_exit = random.randrange(0, biggest_tunnel_exit)
            ind.append((open_or_close,which_exit))
        individuals.append(ind)
    return individuals
def evaluate_individual(ind,room = 'AA'):
    t = 30
    i = 0
    total_flow = 0
    while t >0:
        valve, which_exit = ind[i]
        if valve and cave_system[room]['valve_closed']:
            t-=1
            cave_system[room]['valve_closed'] = False
            total_flow += cave_system[room]['flow_rate']*t

        room = cave_system[room]['exits'][which_exit % len(cave_system[room]['exits'])]
        t-=1
        i+=1
        if i >= len(ind):
            break
    for r in cave_system:
        cave_system[r]['valve_closed'] = True

    return total_flow

def breed(ind1,ind2):
    split_index = random.randint(0,30)
    child1 = []
    child2 = []
    for i in range(len(ind1)):
        if random.randint(0,2)==0:
            child1.append(ind1[i])
            child2.append(ind2[i])
        else:
            child1.append(ind2[i])
            child2.append(ind1[i])
    def mutate(child):
        mutated_child = []
        for (o,e) in child:
            if random.random() < 0.05:
                o = not o
            if random.random() < 0.05:
                e += 1 if random.randint(0,2) ==0 else 2
            mutated_child.append((o,e))
        return mutated_child
    return mutate(child1),mutate(child2)
best_attempt = 0
for attempts in range(1000):
    population_size = 12
    individuals = create_population(population_size)
    prev_best = 0
    num_conseq = 0
    for epochs in range(5000):
        individuals.sort(key=evaluate_individual,reverse=True)
        individuals = individuals[:int(population_size/2)]
        next_individuals = []
        curr_best = evaluate_individual(individuals[0])
        if curr_best == prev_best:
            num_conseq +=1
            if num_conseq > 20:
                break
        else:
            num_conseq =0 
            if curr_best > prev_best:
                prev_best = curr_best
        for i in range(1,int(population_size/2),2):
            c1,c2 = breed(individuals[i],individuals[i-1])
            next_individuals.append(c1)
            next_individuals.append(c2)
        next_individuals.extend(individuals)
        individuals = next_individuals    
        
    individuals.sort(key=evaluate_individual,reverse=True)
    best_attempt = max(best_attempt, evaluate_individual(individuals[0]))

print(best_attempt)



print(f'\033[91m','\033[0m') #red print
