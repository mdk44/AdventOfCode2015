print(ord('c'))
print(ord('d'))
print(chr(99))
print(chr(100))

inp = 'hepxcrrq'

password = []
for i in range(0,len(inp)):
    password.append(inp[i])

print(password)

# Requirements:
# -Increment by 1
# -Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz.
# -Exclude i, o, or l
# -Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz