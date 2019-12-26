import re

# input_file = 'Day 15\\Input.csv'
input_file = 'Day 15\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

for line in lines:
    print(line)

ingred = []
cap = []
dur = []
flv = []
tex = []
cal = []
factors = []
for line in lines:
    numbers = re.findall(r"\-?\d+",line)
    ingred.append(line.split(' ')[0][:-1])
    cap.append(int(numbers[0]))
    dur.append(int(numbers[1]))
    flv.append(int(numbers[2]))
    tex.append(int(numbers[3]))
    cal.append(int(numbers[4]))
    factors.append(0)

factors[0] = 44
factors[1] = 56
for i in range(0,len(ingred)):
    # do stuff