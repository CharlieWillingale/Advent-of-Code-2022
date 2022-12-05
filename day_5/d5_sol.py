import re
from utils import read_input

# Load input
input = read_input('./day_5/input.txt')

#
# Part 1 solution
#

def part1():
    # find number of stacks in input
    num_stacks = 0
    for line in input:
        try:
            if line.strip()[0] == '1':
                num_stacks = len(line.strip().replace(' ',''))
                break

        except IndexError:
            pass

    # create list of stacks for each stack
    stacks = []

    for i in range(0, num_stacks):
        stacks.append([])

    # Fill stckas w/ initial configuration
    for line in input:
        
    
        if len(line.strip()) > 1 and line.strip()[0] != '1':
            line = re.sub(r'\s{3}',r' - ',line)
            for item in range(0,len(line.split())):
                if line.split()[item] != '-':
                    stacks[item].append(line.split()[item].strip('[').strip(']'))

        else:
            break

    for stack in stacks:
        stack.reverse()

    #  Complete actions   
    for line in input:
        
        if len(line.split()) > 0 and line.split()[0] == 'move':
            instructions = line.split()
            num_move = int(instructions[1])
            move_from = int(instructions[3]) - 1
            move_to = int(instructions[5]) - 1

            for moves in range(0, num_move):

                top_item = stacks[move_from].pop(-1)
                stacks[move_to].append(top_item)

    for stack in stacks:
        print(stack.pop(),end='')


#
# Part 2 solution
#

def part2():
    # find number of stacks in input
    num_stacks = 0
    for line in input:
        try:
            if line.strip()[0] == '1':
                num_stacks = len(line.strip().replace(' ',''))
                break

        except IndexError:
            pass

    # create list of stacks for each stack
    stacks = []

    for i in range(0, num_stacks):
        stacks.append([])

    # Fill stckas w/ initial configuration
    for line in input:
        
    
        if len(line.strip()) > 1 and line.strip()[0] != '1':
            line = re.sub(r'\s{3}',r' - ',line)
            for item in range(0,len(line.split())):
                if line.split()[item] != '-':
                    stacks[item].append(line.split()[item].strip('[').strip(']'))

        else:
            break

    for stack in stacks:
        stack.reverse()

    #  Complete actions   
    for line in input:
        
        if len(line.split()) > 0 and line.split()[0] == 'move':
            instructions = line.split()
            num_move = int(instructions[1])
            move_from = int(instructions[3]) - 1
            move_to = int(instructions[5]) - 1

            move_stack = []
            for moves in range(0, num_move):

                top_item = stacks[move_from].pop(-1)
                move_stack.append(top_item)

            for item in move_stack[::-1]:  
                stacks[move_to].append(item)

    for stack in stacks:
        print(stack.pop(),end='')

part1()
print()
part2()
