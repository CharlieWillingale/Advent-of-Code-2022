from utils import read_input

# Load input
input = read_input('./input.txt')

#
# Part 1 solution
#

def signal_strength(x_regiser: int, current_ticks:int) -> int:

    return (x_regiser * current_ticks)

def addx(x_register:int, value: int, current_ticks: int, interesting_strengths:list) -> list:

    for i in range(1,3):
        current_ticks += 1

        
        # check if 'interesting' tick number
        if current_ticks == 20 or (current_ticks - 20) % 40 == 0:
            interesting_strengths.append(signal_strength(x_register,current_ticks))
            # print(current_ticks, x_register)

        if i == 2:
            x_register += value
    
    return (x_register, current_ticks)

def noop(x_register:int, current_ticks: int, interesting_strengths:list) -> int:

    current_ticks += 1

    # check if 'interesting' tick number
    if current_ticks == 20 or (current_ticks - 20) % 40 == 0:
        interesting_strengths.append(signal_strength(x_register,current_ticks))
        # print(current_ticks, x_register)


    return current_ticks


def part1():

    x_register = 1
    ticks = 0
    strength_list = []

    for line in input:

        if line.split()[0] == 'addx':

            x_register, ticks = addx(x_register,int(line.strip().split()[1]),ticks,strength_list)

        else:
            ticks = noop(x_register,ticks,strength_list)

    return sum(strength_list)   


#
# Part 2 solution
#

def addx_2(x_register:int, value: int, current_ticks: int, file) -> list:

    for i in range(1,3):
        current_ticks += 1


        if current_ticks - 1 in list([x_register - 1, x_register, x_register +1]) :
            file.write('#')
        else:
            file.write('.')


        if i == 2:
            x_register += value
    
        if current_ticks % 40 == 0:
            current_ticks = 0

            file.write('\n')

    return (x_register, current_ticks)

def noop_2(x_register:int, current_ticks: int, file) -> int:
    
    current_ticks += 1

    if current_ticks - 1 in list([x_register - 1, x_register, x_register +1]) :
        file.write('#')
    else:
        file.write('.')

    if current_ticks % 40 == 0:
        current_ticks = 0

        file.write('\n')

    return current_ticks

def part2():

    with open('output.txt','w') as f:

        x_register = 1
        ticks = 0
        strength_list = []

        for line in input:

            if line.split()[0] == 'addx':

                x_register, ticks = addx_2(x_register,int(line.strip().split()[1]),ticks,f)

            else:
                ticks = noop_2(x_register,ticks,f)



print(part1())
print(part2())
