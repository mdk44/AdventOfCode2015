input_file = 'Day 19\\Input.csv'
# input_file = 'Day 19\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

inp_string = 'CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl'
# inp_string = 'HOH' # Test, Answer = 4
# inp_string = 'HOHOHO' # Test, Answer = 7

solutions = []

replacements = dict()
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

for src in replacements:
    find_molecules(inp_string, src)

print("Part 1: " + str(len(solutions))) # Correct!
    