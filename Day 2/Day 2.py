import re

class Data_Read:
    def __init__ (self, line):
        numbers = re.findall(r"\d+",line)
        self.l = int(numbers[0])
        self.w = int(numbers[1])
        self.h = int(numbers[2])
        self.paper = 2*self.h*self.w + 2*self.l*self.w + 2*self.h*self.l + min(self.h*self.w, self.h*self.l, self.w*self.l)
        self.ribbon = 2*self.h + 2*self.w + 2*self.l - 2*max(self.w, self.h, self.l) + self.l*self.w*self.h
        # print vars(self)
    def __str__ (self):
        return str(vars(self))

# input_file = 'Day 2\\Day 2 Test 1.txt' # CORRECT
# input_file = 'Day 2\\Day 2 Test 2.txt' # CORRECT
input_file = 'Day 2\\Day 2 Input.txt'
text_file = open(input_file)
lines = text_file.read().split('\n')

paper = 0
ribbon = 0
for line in lines:
    paper += Data_Read(line).paper
    ribbon += Data_Read(line).ribbon

print 'Part 1: ' + str(paper)   # CORRECT
print 'Part 2: ' + str(ribbon)  # CORRECT