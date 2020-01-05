input_file = 'Day 23\\Input.csv'
# input_file = 'Day 23\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

regs = dict()
# regs['a'] = 0 # Part 1
regs['a'] = 1 # Part 2
regs['b'] = 0

def hlf(reg):
    regs[reg] = regs[reg] / 2
    return True

def tpl(reg):
    regs[reg] = regs[reg] * 3
    return True

def inc(reg):
    regs[reg] += 1
    return True


i = 0
try:
    while lines[i] != '':
        inst = lines[i].split(' ')[0]
        if inst == 'hlf':
            reg = lines[i].split(' ')[1]
            hlf(reg)
            i += 1
        elif inst == 'tpl':
            reg = lines[i].split(' ')[1]
            tpl(reg)
            i += 1
        elif inst == 'inc':
            reg = lines[i].split(' ')[1]
            inc(reg)
            i += 1
        elif inst == 'jmp':
            off = lines[i].split(' ')[1]
            if off[0] == "-":
                i -= int(off[1:])
            else:
                i += int(off[1:])
        elif inst == 'jie':
            reg = lines[i].split(' ')[1][0]
            off = lines[i].split(' ')[2]
            if regs[reg] % 2 == 0:
                if off[0] == "-":
                    i -= int(off[1:])
                else:
                    i += int(off[1:])
            else:
                i += 1
        elif inst == 'jio':
            reg = lines[i].split(' ')[1][0]
            off = lines[i].split(' ')[2]
            if regs[reg] == 1:
                if off[0] == "-":
                    i -= int(off[1:])
                else:
                    i += int(off[1:])
            else:
                i += 1
except IndexError:
    print("Register b: " + str(regs['b'])) # Correct!
    exit