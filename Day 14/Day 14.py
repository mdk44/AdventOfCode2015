input_file = 'Day 14\\Input.csv'
# input_file = 'Day 14\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

def calc_dist(speed, time, rest, seconds):
    elapsed = 0
    dist = 0
    flag = 0
    while flag == 0:
        i = 1
        while i <= time:
            elapsed += 1
            dist += speed
            i += 1
            if elapsed > seconds:
                flag = 1
                i += time
        i = 1
        while i <= rest:
            elapsed += 1
            i += 1
            if elapsed > seconds:
                flag = 1
                i += rest
    return dist

deer = []
speed = []
time = []
rest = []
points = []
for line in lines:
    deer.append(line.split(' ')[0])
    speed.append(int(line.split(' ')[3]))
    time.append(int(line.split(' ')[6]))
    rest.append(int(line.split(' ')[13]))
    points.append(0)

results = []
for i in range(0,len(deer)):
    results.append(calc_dist(speed[i],time[i],rest[i],2503))

print("Part 1: " + str(max(results))) # Correct

top_dist = 0
winner = 0
for i in range(0,2503):
    curr_dist = []
    for j in range(0,len(deer)):
        curr_dist.append(calc_dist(speed[j],time[j],rest[j],i))
    curr_dist.append(i)
    for j in range(0,len(deer)):
        if curr_dist[j] == max(curr_dist):
            points[j] += 1

print("Part 2: " + str(max(points))) # Correct