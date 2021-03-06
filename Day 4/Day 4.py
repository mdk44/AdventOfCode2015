import hashlib

input_line = 'bgvyzdsv'
# input_line = 'abcdef' # 609043
# input_line = 'pqrstuv' # 1048970
result = hashlib.md5(input_line.encode())
part1 = result.hexdigest()
part2 = result.hexdigest()

i = 0
while part1[0:5] != '00000':
    new_input_line = input_line + str(i)
    result = hashlib.md5(new_input_line.encode())
    part1 = result.hexdigest()
    if part1[0:6] == '000000':
        part1 = '0123ghf'
    i += 1

print "The MD5 hash for Part 1 is: " + new_input_line + " and the answer is: " + str(i-1) + "." # Correct!

i = 0
while part2[0:6] != '000000':
    new_input_line = input_line + str(i)
    result = hashlib.md5(new_input_line.encode())
    part2 = result.hexdigest()
    if part2[0:7] == '0000000':
        part2 = '0123ghf'
    i += 1

print "The MD5 hash for Part 2 is: " + new_input_line + " and the answer is: " + str(i-1) + "." # Correct!

