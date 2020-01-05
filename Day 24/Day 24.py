from itertools import permutations

input_file = 'Day 24\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

numbers = []
for line in lines:
    numbers.append(int(line))
# numbers = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]

total_weight = 0
for number in numbers:
    total_weight += number
ideal_weight = total_weight / 3

min_quant = 13710311357 # The value when multiplying the 5 largest numbers together
for x in permutations(numbers, 6):
    quant = 1
    if sum(x) == ideal_weight:
        for i in x:
            quant = quant * i
        if quant < min_quant:
            min_quant = quant

print("Part 1: " + str(min_quant)) # Correct!