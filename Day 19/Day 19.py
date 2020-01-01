input_file = 'Day 19\\Input.csv'
# input_file = 'Day 19\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

inp_string = 'CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl'
# inp_string = 'HOH' # Test
# inp_string = 'HOHOHO' # Test

solutions = []

replacements = dict()
repl_p2 = dict()
for line in lines:
    source = line.split(' => ')[0]
    target = line.split(' => ')[1]
    if source not in replacements:
        replacements[source] = []
    replacements[source].append(target)

def replace_letter(inp, sub, repl, nth):
    find = inp.find(sub)
    i = find != -1
    while find != -1 and i != nth:
        find = inp.find(sub, find + 1)
        i += 1
    if i == nth:
        return inp[:find] + repl + inp[find + len(sub):]
    return inp

def count_instances(inp, sub):
    return inp.count(sub, 0, len(inp))

def find_molecules(inp, src): 
    for trg in replacements[src]:
        num = count_instances(inp, src)
        if num != 0:
            for i in range(1, num + 1):
                outp = replace_letter(inp, src, trg, i)
                if outp not in solutions:
                    solutions.append(outp)
    return True

def part_2(inp):
    num = 0
    for i in range(0, len(inp)):
        if inp[i].isupper():
            num += 1
    # The following numbers only appear on the right side, not the left
    num -= inp.count('Rn')
    num -= inp.count('Ar')
    num -= (2*inp.count('Y')) # Related to the pattern in the input file and how removing Y also removes subsequent variables.  Had to google this.
    num -= 1 # To get back to e
    return num

# Part 1
for src in replacements:
    find_molecules(inp_string, src)

print("Part 1: " + str(len(solutions))) # Correct!
print("Part 2: " + str(part_2(inp_string))) # Correct!