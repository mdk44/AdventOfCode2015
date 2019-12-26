input_file = 'Day 14\\Input.csv'
# input_file = 'Day 14\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

def calc_deer(speed, time, rest, seconds):
    elapsed = 0
    dist = 0
    while elapsed <= seconds:
        elapsed += time
        elapsed += rest
        dist += (speed*time)
    return dist
    


deer = []
speed = []
time = []
rest = []
for line in lines:
    deer.append(line.split(' ')[0])
    speed.append(int(line.split(' ')[3]))
    time.append(int(line.split(' ')[6]))
    rest.append(int(line.split(' ')[13]))
    print(line)

results = []
for i in range(0,len(deer)):
    results.append(calc_deer(speed[i],time[i],rest[i],2503))

print("Part 1: " + str(max(results))) # Correct, although I feel like this doesn't account for deer who are running when the clock retires
