input_file = 'Day 7\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

# This is an exercise in creating dynamic dictionaries!

results = dict()
calcs = dict()
results['b'] = 46065 # For part 2.  Comment this line out to get part 1.

def calculate(name):
    try:
        return int(name)
    except ValueError:
        pass # Skip if there is an error in calculating

    for line in lines:
        (ops, result) = line.split('->')
        calcs[result.strip()] = ops.strip().split(' ')

    if name not in results:
        ops = calcs[name]
        if len(ops) == 1: # Returns the direct signal to the resulting wire
            result = calculate(ops[0])
        else:
            op = ops[-2]
            if op == 'AND': # Bitwise AND
                result = calculate(ops[0]) & calculate(ops[2])
            elif op == 'OR': # Bitwise OR
                result = calculate(ops[0]) | calculate(ops[2])
            elif op == 'NOT': # Ensures the result does not get the signal
                result = ~calculate(ops[1]) & 0xffff
            elif op == 'RSHIFT': # Bitwise right shift
                result = calculate(ops[0]) >> calculate(ops[2])
            elif op == 'LSHIFT': # Bitwise left shift
                result = calculate(ops[0]) << calculate(ops[2])
        results[name] = result # Returns the final result to the letter we are checking
    return results[name]

print("The signal sent to wire a is " + str(calculate('a')) + ".") # Correct!  Needed help from reddit though.