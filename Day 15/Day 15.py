import re

input_file = 'Day 15\\Input.csv'
# input_file = 'Day 15\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

for line in lines:
    print(line)

cookies = []
for line in lines:
    cookie = []
    numbers = re.findall(r"\-?\d+",line)
    cookie.append(int(numbers[0]))
    cookie.append(int(numbers[1]))
    cookie.append(int(numbers[2]))
    cookie.append(int(numbers[3]))
    cookie.append(int(numbers[4]))
    cookies.append(cookie)
print(cookies)

best_total = 0
best_for_calories = 0
for i in range(0, 101):
    for j in range(0, 101-i):
        for k in range(0, 101-i-j):
            l = 100 - i - j - k
            total = 1
            # nums = [i*cookies[0][p] + j*cookies[1][p] for p in range(0, 5)] # Test case works
            nums = [i*cookies[0][p] + j*cookies[1][p] + k*cookies[2][p] + l*cookies[3][p] for p in range(0, 5)]
            if min(nums) <= 0:
                continue
            for x in range(0, len(nums)-1):
                total *= nums[x]
            best_total = max(total, best_total)
            if nums[4] == 500:
                best_for_calories = max(total, best_for_calories)

print("Part 1: " + str(best_total)) # Correct
print("Part 2: " + str(best_for_calories)) # Correct