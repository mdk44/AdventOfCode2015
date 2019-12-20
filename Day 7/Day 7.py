input_file = 'Day 7\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

print lines[10]

# 'lr' << 'lt' bitwise left shift
# 'lr' >> 'lt' bitwise right shift
# 'lr' | 'lt' bitwise OR
# 'lr' & 'lt' bitwise AND
# ~ 'lt' bitwise complement