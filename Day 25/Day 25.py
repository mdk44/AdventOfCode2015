row = 2978
column = 3083
init_code = 20151125

def next_code(code):
    return (code * 252533) % 33554393

def get_code(row, column):
	return sum(range(row + column - 1)) + column
    # This calculates the code number to generate:
    #   | 1   2   3   4   5   6  
    # ---+---+---+---+---+---+---+
    # 1 |  1   3   6  10  15  21
    # 2 |  2   5   9  14  20
    # 3 |  4   8  13  19
    # 4 |  7  12  18
    # 5 | 11  17
    # 6 | 16
    # Alternatively could have used num = sum(row - 1, column - 1)
    # Then would return num * (num + 1) / 2 + column (calculating a series sum)

code = get_code(row, column)
curr_code = init_code
for i in range(code - 1):
	curr_code = next_code(curr_code)

print("Part 1: " + str(curr_code)) # Correct!