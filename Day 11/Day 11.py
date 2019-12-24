print(ord('c'))
print(ord('d'))
print(chr(99))
print(chr(100))

def increment(password):
    new_char = 7
    for i in range(len(password)-1,-1,-1):
        if password[i] == 'z':
            password[i] = 'a'
            new_char -= 1
        elif password[i] != 'z':
            pass
    password[new_char] = chr(ord(password[new_char])+1)
    return password

def check_incr(password):
    incr = False
    for i in range(2,len(password)):
        if chr(ord(password[i-2])) == chr(ord(password[i-1])-1) and chr(ord(password[i-1])) == chr(ord(password[i])-1):
            incr = True
    return incr


# inp = 'hepxcrrq'
inp = 'fgcgeuw'

password = []
for i in range(0,len(inp)):
    password.append(inp[i])
print(password)

print(check_incr(password))

# Requirements:
# -Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz.
# -Exclude i, o, or l
# -Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz