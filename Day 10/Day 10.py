from itertools import groupby

def lookandsay(n):
    return ''.join(str(len(list(g))) + k for k, g in groupby(n))

inp = '1113122113'
for i in range(0,40):
    inp = lookandsay(inp)

print("Part 1: " + str(len(inp))) # Correct!

inp = '1113122113'
for i in range(0,50):
    inp = lookandsay(inp)

print("Part 2: " + str(len(inp))) # Correct!