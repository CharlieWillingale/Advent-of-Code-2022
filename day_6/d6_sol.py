from utils import read_input

# Load input
input = read_input('./day_6/input.txt')

#
# Part 1 solution
#

# read input returns a listwith a single element in this instance
input = input[0]

def part1():
    
    # find the first 4 unique characters and return the last position + 1 to account for count starting at 1
    for i,j,k,l in zip(range(0,len(input) - 3),range(1,len(input) - 2),range(2,len(input) - 1),range(3,len(input))):

        chars = [input[i], input[j], input[k], input[l]]

        if chars.count(input[i]) == 1 and chars.count(input[j]) == 1 and chars.count(input[k]) == 1  and chars.count(input[l]) == 1:
            return l + 1
        
#
# Part 2 solution
#

def part2():
    
    # Question requires first 14 unique sequence
    for start_digit in range(0,len(input)-14):

        chars = []

        # Create list of 14 consecutive digits to compare
        for char_pos in range(start_digit, start_digit + 14):
            chars.append(input[char_pos])

        # len set == means the 14 consecutive digits will be unique
        if len(set(chars)) == 14:
            return start_digit + 14

print(part1())
print(part2())
