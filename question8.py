import random

def randnames(num_names):
    names = ["Alice", "Bob", "Lenny","Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Isabel", "Jack", "Lenny", "Molly", "Nathan", "Olivia", "Peter", "Quincy", "Rachel", "Sam", "Tina", "Victor"]
    return random.sample(names, num_names)
station_names = ["Station 1", "Station 2", "Station 3", "Station 4"]
stations = {name: randnames(random.randint(1, 5)) for name in station_names}
lenny_station = None
for station, people in stations.items():
    if "Lenny" in people:
        lenny_station = station
        break
print("Lenny is at {}".format(lenny_station))