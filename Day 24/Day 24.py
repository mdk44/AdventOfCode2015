input_file = 'Day 24\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

numbers = []
for line in lines:
    numbers.append(int(line))

