import re
import sys
import time

# input_file = 'Day 18\\Input.csv'
input_file = 'Day 18\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

grid = dict()
for y in range(0, len(lines)):
    for x in range(0, len(lines[y])):
        grid[y, x] = lines[y][x]