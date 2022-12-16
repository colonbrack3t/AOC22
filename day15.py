rawdata = open("day15input","r").read()
data = rawdata.split('\n')
import time
start_time = time.time()
print('Info: This program takes approx.',f'{92}s','to run')
class sensor():
    centre = ()
    nearest = 0
    beacon = ()
    def __init__(self, centre, beacon):
        self.centre = centre
        self.nearest = sensor.manhattan(self.centre,beacon)
        self.beacon = beacon
    def manhattan(p1,p2):
        return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
    def no_beacon(self,p):
        return sensor.manhattan(self.centre,p)<=self.nearest
    def get_x_boundaries(self):
        # can optimise
        return self.centre[0]-self.nearest, self.centre[0] + self.nearest
    def get_y_coverage(self,y_level):
        dist_from_y = abs(self.centre[1] - y_level)
        if dist_from_y<self.nearest:
            return self.centre[0] + (dist_from_y-self.nearest), self.centre[0] - (dist_from_y-self.nearest)
        else:
            return None
    def perimeter(self, max_size = 20):
        return [(x + self.centre[0], y + self.centre[1]) for x , y in zip(range(self.nearest+2),range(self.nearest+1,-1,-1)) if x + self.centre[0] <= max_size and y + self.centre[1] <= max_size]
            
def parse_data(s):
    return tuple(map(lambda x : int(x.split('=')[1]) ,s.split('at')[1].split(',')))

sensors = []
min_x = 100
max_x = 0
y = 2000000
ranges = set()
beacons = set()
possible_beacon_locations = set()
for d in data:
    sensor_centre, beacon = tuple(map(parse_data, d.split(':')))
    s = sensor(sensor_centre,beacon)
    sensors.append(s)
    #small_x,big_x = s.get_x_boundaries()
    #min_x =min(small_x,min_x)
    #max_x = max(max_x,big_x)
    r = s.get_y_coverage(y)
    pers = s.perimeter(4000000)
    for p in pers:
        possible_beacon_locations.add(p)
    if r is not None:
        for x in range(r[0],r[1]+1):
            ranges.add(x)
    if beacon[1] == y:
        beacons.add(beacon)
distress_beacon_signal = 0
print(f'\033[91m{len(ranges)-len(beacons)}','\033[0m')
print('Still working...')
for p in possible_beacon_locations:
    in_sensor_range = False
    for s in sensors:
        if s.no_beacon(p):
            in_sensor_range = True
            break
    if not in_sensor_range:
        distress_beacon_signal = (p[0] * 4000000) + p[1]
        break
    
    



print(f'\033[91m{distress_beacon_signal}','\033[0m') #red print
