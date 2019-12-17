input_file = 'Day 5\\Input.csv'
text_file = open(input_file)
# lines = text_file.read().split('\n')
lines = []
lines.append('ugknbfddgicrmopn')

print lines[0]

def find_vowels(string):
    num_vowels = 0
    for i in string:
        if i.upper() == 'A' or i.upper() == 'E' or i.upper() == 'I' or i.upper() == 'O' or i.upper() == 'U':
            num_vowels += 1
    return num_vowels

def find_doubles(string):
    num_doubles = 0
    for i in range(1, len(string)):
        if string[i - 1].upper() == string[i].upper():
            num_doubles += 1
    return num_doubles

def find_bad(string):
    num_bad = 0
    if 'ab' in string or 'cd' in string or 'pq' in string or 'xy' in string:
        num_bad += 1
    return num_bad

def naughty_or_nice(string):
    if find_vowels(string) > 2 and find_doubles(string) > 0 and find_bad(string) == 0:
        nice = 1
    else:
        nice = 0
    return nice

print naughty_or_nice(lines[0])