import re

# Load input for the games
# with open('./input.txt','r') as f:
with open('./day_6/input.txt','r') as f:

    input = f.readlines()

#
# Part 1 solution
#

input = input[0]

print(input)

def part1():
    
    for i,j,k,l in zip(range(0,len(input) - 3),range(1,len(input) - 2),range(2,len(input) - 1),range(3,len(input))):

        chars = [input[i], input[j], input[k], input[l]]

        if chars.count(input[i]) == 1 and chars.count(input[j]) == 1 and chars.count(input[k]) == 1  and chars.count(input[l]) == 1:
            return l + 1
        
#
# Part 2 solution
#

def part2():
    
    for start_digit in range(0,len(input)-14):

        chars = []

        for char_pos in range(start_digit, start_digit + 14):
            chars.append(input[char_pos])

        if len(set(chars)) == 14:
            return start_digit + 14

print(part1())
print(part2())
