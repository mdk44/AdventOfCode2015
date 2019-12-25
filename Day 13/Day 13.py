from itertools import permutations

input_file = 'Day 13\\Input.csv'
# input_file = 'Day 13\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

people = []
seating = dict()
for line in lines:
    p1 = line.split(' ')[0]
    p2 = line.split(' ')[10][:-1]
    effect = line.split(' ')[2]
    if effect == 'lose':
        num = int(line.split(' ')[3])*-1
    else:
        num = int(line.split(' ')[3])
    seating[p1,p2] = num
    if p1 not in people:
        people.append(p1)
    if p2 not in people:
        people.append(p2)

perm = permutations(people)
max_happy = 0
for item in list(perm):
    happiness = 0
    happiness += seating[item[0],item[len(item)-1]]
    happiness += seating[item[len(item)-1],item[0]]
    for i in range(1,len(item)):
        happiness += seating[item[i],item[i-1]]
        happiness += seating[item[i-1],item[i]]
    if happiness > max_happy:
        max_happy = happiness

print("Part 1: " + str(max_happy)) # Correct!

for person in people:
    seating[person,'Matt'] = 0
    seating['Matt', person] = 0
people.append('Matt')

perm = permutations(people)
max_happy = 0
for item in list(perm):
    happiness = 0
    happiness += seating[item[0],item[len(item)-1]]
    happiness += seating[item[len(item)-1],item[0]]
    for i in range(1,len(item)):
        happiness += seating[item[i],item[i-1]]
        happiness += seating[item[i-1],item[i]]
    if happiness > max_happy:
        max_happy = happiness

print("Part 2: " + str(max_happy)) # Correct!



