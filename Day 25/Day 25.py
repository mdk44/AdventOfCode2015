row = 2978
column = 3083
init_code = 20151125

def next_code(code):
    return (code * 252533) % 33554393

def get_code(row, column):
	return sum(range(row + column - 1)) + column

code = get_code(row, column)
curr_code = init_code
for i in range(code - 1):
	curr_code = next_code(curr_code)

print("Part 1: " + str(curr_code)) # Correct!