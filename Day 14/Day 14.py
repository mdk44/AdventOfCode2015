# input_file = 'Day 14\\Input.csv'
input_file = 'Day 14\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

def calc_deer(deer, speed, time, rest):
    #do stuff
    #return stuff

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

# for dr in deer:
#     results.append(calc_deer(dr))

# do something like this