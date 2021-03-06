import re
import sys
import time
from PIL import Image, ImageDraw

input_file = 'Day 6\\Input.csv'
output_file = 'Day 6\\Lights.png'
text_file = open(input_file)
lines = text_file.read().split('\n')

class Data_Read:
    def __init__ (self, line):
        numbers = re.findall(r"[+-]?\d+(?:\.\d+)?",line)
        self.x1 = int(numbers[0])
        self.y1 = int(numbers[1])
        self.x2 = int(numbers[2])
        self.y2 = int(numbers[3])
        # print vars(self)
    def __str__ (self):
        return str(vars(self))


def image_grid(grid):
    off = (0, 0, 0)
    on = (226, 25, 224)
    width = 5000
    height = 5000
    img = Image.new('RGB', (width, height), color = off)
    dr = ImageDraw.Draw(img)
    for y in grid:
        for x in grid[y]:
            if grid[y][x] == OFF:
                dr.rectangle(((5*x,5*y),(5*x+5,5*y+5)),fill=off)
            elif grid[y][x] == ON:
                dr.rectangle(((5*x,5*y),(5*x+5,5*y+5)),fill=on)
    img.save(output_file)

def toggle_lights(grid, start_x, start_y, end_x, end_y):
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            if grid[y][x] == OFF:
                grid[y][x] = ON
            elif grid[y][x] == ON:
                grid[y][x] = OFF

def on_lights(grid, start_x, start_y, end_x, end_y):
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            grid[y][x] = ON

def off_lights(grid, start_x, start_y, end_x, end_y):
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            grid[y][x] = OFF

def toggle_lights2(grid, start_x, start_y, end_x, end_y):
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            grid[y][x] += 2

def on_lights2(grid, start_x, start_y, end_x, end_y):
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            grid[y][x] += 1

def off_lights2(grid, start_x, start_y, end_x, end_y):
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            grid[y][x] -= 1
            if grid[y][x] < 0:
                grid[y][x] = 0

# Part 1
OFF = 1
ON = 2

grid = {}
for y in range(0,1000):
    grid[y] = {}
    for x in range(0,1000):
        grid[y][x] = OFF

for i in range(0, len(lines)):
    start_x = Data_Read(lines[i]).x1
    start_y = Data_Read(lines[i]).y1
    end_x = Data_Read(lines[i]).x2
    end_y = Data_Read(lines[i]).y2
    if "turn on" in lines[i]:
        on_lights(grid,start_x,start_y,end_x,end_y)
    elif "turn off" in lines[i]:
        off_lights(grid,start_x,start_y,end_x,end_y)
    if "toggle" in lines[i]:
        toggle_lights(grid,start_x,start_y,end_x,end_y)

image_grid(grid)

count_lights = 0
for y in grid:
    for x in grid[y]:
        if grid[y][x] == ON:
            count_lights += 1
    
# Part 2
grid2 = {}
for y in range(0,1000):
    grid2[y] = {}
    for x in range(0,1000):
        grid2[y][x] = 0

for i in range(0, len(lines)):
    start_x = Data_Read(lines[i]).x1
    start_y = Data_Read(lines[i]).y1
    end_x = Data_Read(lines[i]).x2
    end_y = Data_Read(lines[i]).y2
    if "turn on" in lines[i]:
        on_lights2(grid2,start_x,start_y,end_x,end_y)
    elif "turn off" in lines[i]:
        off_lights2(grid2,start_x,start_y,end_x,end_y)
    if "toggle" in lines[i]:
        toggle_lights2(grid2,start_x,start_y,end_x,end_y)

sum_lights = 0
for y in grid2:
    for x in grid2[y]:
        sum_lights += grid2[y][x]

print "Part 1: " + str(count_lights) # Correct!
print "Part 2: " + str(sum_lights) # Correct!