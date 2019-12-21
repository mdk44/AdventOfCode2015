from itertools import permutations

input_file = 'Day 9\\Input.csv'
# input_file = 'Day 9\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

cities = []
city_dist = dict()

for line in lines:
    city1 = line.split(' ')[0]
    city2 = line.split(' ')[2]
    dist = int(line.split(' ')[4])
    city_dist[city1,city2] = dist
    if city1 not in cities:
        cities.append(city1)
    if city2 not in cities:
        cities.append(city2)

results = []
perm = permutations(cities)
for item in list(perm):
    new_dist = 0
    for i in range(1,len(item)):
        try:
            new_dist += city_dist[item[i],item[i-1]]
        except KeyError:
            new_dist += city_dist[item[i-1],item[i]]
    results.append(new_dist)

print("Part 1: " + str(min(results))) # Correct
print("Part 2: " + str(max(results))) # Correct