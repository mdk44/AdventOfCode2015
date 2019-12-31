import re
import sys

input_file = 'Day 18\\Input.csv'
# input_file = 'Day 18\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

grid = dict()
for y in range(0, len(lines)):
    for x in range(0, len(lines[y])):
        grid[y, x] = lines[y][x]

def print_grid(grid):
    for y in range(0, len(lines)):
        grid_line = ""
        for x in range(0, len(lines[y])):
            grid_line += grid[y, x]
        print(grid_line)

def check_lights(grid, y, x):
    on = 0
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            if (i, j) not in grid:
                continue
            if i == y and x == j:
                continue
            if grid[i,j] == '#':
                on += 1
    return on

def switch_light(grid, y, x):
    if grid[y, x] == '#':
        if check_lights(grid, y, x) not in (2, 3):
            return '.'
        else:
            return '#'
    elif grid[y, x] == '.':
        if check_lights(grid, y, x) == 3:
            return '#'
        else:
            return '.'

def switch_light_p2(grid, y, x):
    if (y, x) in [(0, 0), (0, 99), (99, 0), (99, 99)]:
        return '#'
    elif grid[y, x] == '#':
        if check_lights(grid, y, x) not in (2, 3):
            return '.'
        else:
            return '#'
    elif grid[y, x] == '.':
        if check_lights(grid, y, x) == 3:
            return '#'
        else:
            return '.'

# steps = 4
steps = 100

for i in range(0, steps):
    new_grid = dict()
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            # new_grid[y, x] = switch_light(grid, y, x) # Part 1
            new_grid[y, x] = switch_light_p2(grid, y, x) # Part 2
    grid = new_grid
    i += 1
    
# print_grid(grid)
num_on = 0
for (y, x) in grid:
    if grid[y, x] == '#':
        num_on += 1

print("Answer: " + str(num_on)) # Correct for Parts 1 and 2!