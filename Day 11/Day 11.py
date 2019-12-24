def increment(password):
    new_char = 7
    for i in range(len(password)-1,-1,-1):
        if password[i] == 'z':
            password[i] = 'a'
            new_char -= 1
        elif password[i] != 'z':
            pass
    if chr(ord(password[new_char])+1) == 'i' or chr(ord(password[new_char])+1) == 'o' or chr(ord(password[new_char])+1) == 'l':
        password[new_char] = chr(ord(password[new_char])+2)
    else:
        password[new_char] = chr(ord(password[new_char])+1)
    return password

def check_incr(password):
    # Must return True to be satisfied
    incr = False
    for i in range(2,len(password)):
        if chr(ord(password[i-2])) == chr(ord(password[i-1])-1) and chr(ord(password[i-1])) == chr(ord(password[i])-1):
            incr = True
    return incr

def check_doubles(password):
    doubles = 0
    for i in range(1,len(password)): # Counts number of doubles
        if chr(ord(password[i-1])) == chr(ord(password[i])):
            doubles += 1
    for i in range(2,len(password)): # Subtracts number of triples to remove overlap
        if chr(ord(password[i-2])) == chr(ord(password[i-1])) and chr(ord(password[i-1])) == chr(ord(password[i])):
            doubles -= 1
    for i in range(3,len(password)): # Adds one back if there are 4 consecutive letters (I THINK this is the rule)
        if chr(ord(password[i-3])) == chr(ord(password[i-2])) and chr(ord(password[i-2])) == chr(ord(password[i-1])) and chr(ord(password[i-1])) == chr(ord(password[i])):
            doubles += 1
    return doubles

def check_password(password):
    valid = False
    if check_incr(password) == True and check_doubles(password) > 1:
        valid = True
    return valid

inp = 'hepxcrrq'

password = []
for i in range(0,len(inp)):
    password.append(inp[i])
print(password)

print(check_password(password))

# Part 1
flag = 0
while flag == 0:
    increment(password)
    if check_password(password) == True:
        flag += 1

print("Part 1: " + password[0] + password[1] + password[2] + password[3] + password[4] + password[5] + password[6] + password[7])