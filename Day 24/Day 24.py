from itertools import permutations

input_file = 'Day 24\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

numbers = []
for line in lines:
    numbers.append(int(line))
# numbers = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11] # Test input

total_weight = 0
for number in numbers:
    total_weight += number
# ideal_weight = total_weight / 3 # Part 1
ideal_weight = total_weight / 4 # Part 2

min_quant = 15000000000
# for x in permutations(numbers, 6): # Part 1
for x in permutations(numbers, 4): # Part 2
    quant = 1
    if sum(x) == ideal_weight:
        for i in x:
            quant = quant * i
        if quant < min_quant:
            min_quant = quant

print("Answer: " + str(min_quant)) # Correct!