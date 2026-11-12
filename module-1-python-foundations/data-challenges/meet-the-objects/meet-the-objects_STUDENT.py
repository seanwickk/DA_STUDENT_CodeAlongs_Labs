#!/usr/bin/env python3
"""Meet the Objects: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "bike_stations.json"  # edit the filepath with the data
with open(DATA_FILE) as f:
    stations = json.load(f)

# Step 0, answer 1:
# Data on a current station
# Step 0, answer 2:
# Capacity holds numbers wjile Station id hold texts
# Step 0, answer 3:
#  some stations have avaible bikes while stating it does need maintenance


# ===== Day 1 =====

# Step 1: Reproduce the Parallel-List Bug and Name the Wrong Stations
# TODO: assign `names` and `bikes` to two empty lists
names = []
bikes = []
# TODO: loop over `stations`; append each one's "name" to `names`
for station in stations:
    names.append(station['name'])
    bikes.append(station['bikes_available'])
# TODO: append the same station's "bikes_available" to `bikes`
names.pop(2)

print("stations in the file:", len(stations))
# TODO: loop over range(len(names)); print names[i], "|", bikes[i], "bikes"
for i in range(len(names)):
    print (names[i], "|", bikes[i], "bikes")

# Step 1, answer 1:
# The data shows us bike stations across New York City. In each location it contains important information on the station, like a name, amount of bikes able to be docks.
# Step 1, answer 2:
# .pop(2) removes the third index of the list since pythons starts at 0 for counting fields.
# Step 1, answer 3:
# People never see the actually maintenance needed or not on a station.

# Step 2: Define the Station Class and Prove Two Instances Are Independent

class Station:
    def __init__(self, station_id, name, capacity, bikes_available, needs_maintenance):
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.needs_maintenance = needs_maintenance
        self.station_id = station_id
    
    def needs_restocks(self):
        return self.bikes_available < self.capacity / 4
        
    # TODO: add __init__ with name (str), capacity and bikes_available (int)
    # TODO: in __init__, assign each parameter to self.<same name>
    # TODO: add a parameter and self.<name> for each extra field you agreed
    # TODO: add needs_restock(self): True if bikes_available < capacity / 4
    pass

fleet = []
for s in stations:
    fleet.append(Station(s["name"], s["capacity"], s["bikes_available"]))
busy = fleet[0]
quiet = fleet[2]
#print(busy.needs_restocks())
#print(quiet.needs_restocks())
# TODO: assign `fleet` to []; loop over `stations` as `s`
# TODO: append Station(s["name"], s["capacity"], s["bikes_available"])
# TODO: assign `busy`, `quiet` to two stations with equal needs_restock()
# TODO: print both needs_restock() answers
# TODO: set busy.bikes_available to 0, then print both answers again
busy.bikes_available = 0
print(busy.needs_restocks())
print(quiet.needs_restocks())
# Step 2, answer 1:
#True
#False
# Step 2, answer 2:
# The two lists differed by providing different indexes of the original list; busy kept the third index while quiet contained the first one.
#
# Step 2, answer 3:
# The fields left out were station IDs and whether the depot needed maintenance. We don't need maintenance because it contains inaccurate data that could give false information, and the station ID isn't needed since we can already identify each station by its unique name.
# Step 2, answer 4:
# Before setting busy.bikes_available to 0, both busy.needs_restock() and quiet.needs_restock() printed the exact same answer (False / True). After changing busy.bikes_available to 0, busy.needs_restock() changed to True while quiet.needs_restock() stayed the same (False). This proves the two stations are independent objects because modifying one does not change the other.



# ===== Day 2 =====

# Step 3: Add `__str__` and Find Out Which of Four Prints It Changes

class Station:
    def __init__(self, station_id, name, capacity, bikes_available, needs_maintenance):
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.needs_maintenance = needs_maintenance
        self.station_id = station_id
    
    def needs_restocks(self):
        return self.bikes_available < self.capacity / 4
    
    def __str__(self):
        return f"{self.name}: {self.bikes_available} of {self.capacity} bikes"

fleet = []
for s in stations:
    fleet.append(Station(s["name"], s["capacity"], s["bikes_available"], s["needs_maintenance"], s["station_id"]))

# TODO: copy your Station class from Step 2 here
# TODO: add __str__(self) to return text like "Grand Army Plaza: 6 of 48 bikes"
# TODO: build it from self.name, self.bikes_available and self.capacity
# TODO: rebuild `fleet` from this class with the same loop as Step 2

print(fleet[0])
print(fleet[:2])

# Step 3, answer 1:
#
# Step 3, answer 2:
#


# Step 4: Add `__repr__` and Print the Van List for You and the Dispatcher
class Station:
    def __init__(self, station_id, name, capacity, bikes_available, needs_maintenance):
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.needs_maintenance = needs_maintenance
        self.station_id = station_id
    
    def needs_restocks(self):
        return self.bikes_available < self.capacity / 4
    
    def __str__(self):
        return f"{self.name}: {self.bikes_available} of {self.capacity} bikes"
    def __repr__(self):
        return f"Station('{self.name}', {self.bikes_available})"
  
    fleet = []
for s in stations:
    fleet.append(Station(s["name"], s["capacity"], s["bikes_available"], s["needs_maintenance"], s["station_id"]))

# TODO: copy your Station class from Step 3 here
# TODO: add __repr__(self) to return text like "Station('Grand Army Plaza', 6)"
# TODO: rebuild `fleet` from this class with the same loop as Step 2
# TODO: assign `van_list` to []; loop over `fleet`
# TODO: append each station whose needs_restock() returns True to `van_list`
van_list = []

for needed_help in fleet:
    if needed_help.needs_restock():
        van_list.append(needed_help)


print(van_list)
for station in van_list:
    print(station)

# Step 4, answer 1:
#
# Step 4, answer 2:
# __str__ is used to be printed for views while __repr__ provide information for programmer or the computer to read and also use.
# Step 4, answer 3:
# I would hand the __str__ printout to the dispatcher/van driver because it is clean, easy to read, and clearly shows how many bikes each station needs. I would keep the __repr__ printout for myself (the programmer) because it shows the exact object structure and code details needed for debugging.
