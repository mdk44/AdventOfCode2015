import itertools

input_file = 'Day 17\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')
# lines = [20, 15, 10, 5, 5] # Test case

numbers = []
for line in lines:
    numbers.append(int(line))

def fill_nog(lines):
    # result = [seq for i in range(len(lines), 0, -1) for seq in itertools.combinations(lines, i) if sum(seq) == 25] # Test case
    result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq) == 150]
    return len(result)

def fill_nog_p2(lines):
    result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq) == 150]
    min_num = 999
    min_count = 0
    for i in result:
        min_num = min(min_num, len(i))
    for j in result:
        if len(j) == min_num:
            min_count += 1
    return min_count

print("Part 1: " + str(fill_nog(lines))) # Correct!
print("Part 2: " + str(fill_nog_p2(lines))) # Correct!