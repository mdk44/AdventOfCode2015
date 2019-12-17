input_file = 'Day 5\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')
# lines = [] # all test results are correct
# lines.append('ugknbfddgicrmopn')
# lines.append('aaa')
# lines.append('jchzalrnumimnmhp')
# lines.append('haegwjzuvuyypxyu')
# lines.append('dvszwmarrgswjxmb')

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
        result = "Nice"
    else:
        result = "Naughty"
    return result

#Part 1
total_nice_p1 = 0
for i in range(0, len(lines)):
    if naughty_or_nice(lines[i]) == "Nice":
        total_nice_p1 += 1

print "Part 1: " + str(total_nice_p1)  # Correct!