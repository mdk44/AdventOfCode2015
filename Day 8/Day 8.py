input_file = 'Day 8\\Input.csv'
# input_file = 'Day 8\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

string_code = 0
in_memory = 0
newly_encoded = 0

for line in lines:
    in_memory += len(eval(line))
    string_code += len(line)
    newly_encoded += 2
    newly_encoded += line.count('\\')
    newly_encoded += line.count('"')

print("Part 1: " + str(string_code - in_memory)) # Correct!
print("Part 2: ") + str(newly_encoded) # Correct!
