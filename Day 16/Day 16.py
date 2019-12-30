import re

input_file = 'Day 16\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

sue = dict()
sue['children:'] = 3
sue['cats:'] = 7
sue['samoyeds:'] = 2
sue['pomeranians:'] = 3
sue['akitas:'] = 0
sue['vizslas:'] = 0
sue['goldfish:'] = 5
sue['trees:'] = 3
sue['cars:'] = 2
sue['perfumes:'] = 1

def check_p1(types, value):
    value = int(value)
    return sue[types] == value

def check_p2(types, value):
    value = int(value)
    if types in ("cats:", "trees:"):
        return sue[types] < value
    elif types in ("pomeranians:", "goldfish:"):
        return sue[types] > value
    return sue[types] == value

for line in lines:
    line = line.strip("\n").split()
    sue_num = line[1][:-1]
    type1 = line[2]
    val1 = line[3].strip(',')
    type2 = line[4]
    val2 = line[5].strip(',')
    type3 = line[6]
    val3 = line[7].strip(',')
    if (check_p1(type1, val1) and check_p1(type2, val2) and check_p1(type3, val3)):
        print("Part 1: " + str(sue_num)) # Correct!
    if (check_p2(type1, val1) and check_p2(type2, val2) and check_p2(type3, val3)):
        print("Part 2: " + str(sue_num)) # Correct!