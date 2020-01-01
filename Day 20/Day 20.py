import math

inp = 34000000
# inp = 120

def get_elves(house):
    visit1 = [i for i in range(1, int(math.sqrt(house)) + 1) if house % i == 0] # Elf visits this house if mod of house / elf = 0, ceiling of sqrt(house)
    visit2 = [house / v for v in visit1 if house != v * v] # Elf visits this house but stops at sqrt(house) to prevent double-counting houses
    return visit1 + visit2

part_one, part_two = None, None
i = 0
while not part_one or not part_two:
    i += 1
    houses = get_elves(i)
    if not part_one:
        if sum(houses) * 10 >= inp:
            part_one = i
    if not part_two:
        if sum(h for h in houses if i / h <= 50) * 11 >= inp:
            part_two = i

print("Part 1: " + str(part_one)) # Correct!
print("Part 2: " + str(part_two)) # Correct!