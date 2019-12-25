import re
from json import loads

input_file = 'Day 12\\Input.csv'
text_file = open(input_file)
lines = text_file.read()

sum_p1 = 0

numbers = re.findall(r"\-?\d+",lines)
for i in range(0,len(numbers)):
    sum_p1 += int(numbers[i])

print("Part 1: " + str(sum_p1)) # Correct!

def n(inp):
    if type(inp) == int:
        return inp
    if type(inp) == list:
        return sum([n(inp) for inp in inp])
    if type(inp) != dict:
        return 0
    if 'red' in inp.values():
        return 0
    return n(list(inp.values()))

print("Part 2: " + str(n(loads(lines)))) # Correct!