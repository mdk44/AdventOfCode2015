input_file = 'Day 3\\Input.csv'
text_file = open(input_file)
lines = list(text_file.read())
# lines = list('^v^v^v^v^v')
# lines = list('^>v<')

x = 0
y = 0
presents = 1
coords = []
coords.append([0,0])
for i in range(0, len(lines)):
    skip = 0
    if lines[i] == '^':
        y -= 1
    elif lines[i] == 'v':
        y += 1
    elif lines[i] == '<':
        x -= 1
    elif lines[i] == '>':
        x += 1
    curr_coord = [x,y]
    for j in range(0, len(coords)):
        if coords[j] == curr_coord:
            skip += 1
    if skip == 0:
        coords.append(curr_coord)
        presents += 1

print "Part 1: " + str(presents) # Correct!

santa_x = 0
santa_y = 0
robo_x = 0
robo_y = 0
presents = 1
coords = []
coords.append([0,0])
for i in range(0, len(lines)):
    if i % 2 == 0: # Even, moves Santa
        skip = 0
        if lines[i] == '^':
            santa_y -= 1
        elif lines[i] == 'v':
            santa_y += 1
        elif lines[i] == '<':
            santa_x -= 1
        elif lines[i] == '>':
            santa_x += 1
        curr_coord = [santa_x,santa_y]
        for j in range(0, len(coords)):
            if coords[j] == curr_coord:
                skip += 1
        if skip == 0:
            coords.append(curr_coord)
            presents += 1
    elif i % 2 != 0: # Odd, moves Robo-Santa
        skip = 0
        if lines[i] == '^':
            robo_y -= 1
        elif lines[i] == 'v':
            robo_y += 1
        elif lines[i] == '<':
            robo_x -= 1
        elif lines[i] == '>':
            robo_x += 1
        curr_coord = [robo_x,robo_y]
        for j in range(0, len(coords)):
            if coords[j] == curr_coord:
                skip += 1
        if skip == 0:
            coords.append(curr_coord)
            presents += 1

print "Part 2: " + str(presents) # Correct!