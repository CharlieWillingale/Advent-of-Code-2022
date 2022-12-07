from utils import read_input

# Load input
input = read_input('./day_7/input.txt')



# 
# Rules
# 
# if line[0] == $: command
# cd, ls: same as terminal
# 
# Find the size of each dir and return the sum of those < 100000


#
# Part 1 solution
#

def part1():

    dir_count = 0 # For debugging

    # Create list of directories in the input
    dir_list = []
    line_count = 0

    amended_input = []
    for line in input:
        line_count += 1

        if line.split()[1] == 'cd' and line.split()[2] != '..':

            if line.split()[2] in dir_list:
                amended_input.append(line.strip() + '**' + str(line_count))

            else:
                amended_input.append(line.strip())

            dir_list.append(amended_input[-1].split()[2])
            dir_count += 1
        else:
            amended_input.append(line.strip())

    # For eaach directory in dir_list, creating a corresponding list of the directory size
    dir_size = []
    for dir in dir_list:
        
        in_dir_flag = False # To ensure we start at the correct point for the current directory
        file_path = [] # Track current position in directory
        current_size = 0 # Current size of working directory
        
        for line in amended_input:
            
            if line.strip() == '$ cd ' + dir:
                in_dir_flag = True    
                
            if in_dir_flag:
                if line.split()[0] == '$': 

                            if line.split()[1] == 'cd' and line.split()[2] != '..':
                                file_path.append(line.split()[2])

                            elif line.split()[1] == 'cd' and file_path[-1] == dir:
                                break

                            elif line.split()[1] == 'cd' and file_path[-1] != dir:
                                file_path.pop()

                elif line.split()[0] == 'dir':
                    pass

                else:
                    current_size += int(line.split()[0])

        dir_size.append(current_size)

        solution = 0
        for x in dir_size:
            if x < 100_000:
                solution += x

    return solution

     #
# Part 1 solution
#

def part2():

    dir_count = 0 # For debugging

    # Create list of directories in the input
    dir_list = []
    line_count = 0

    amended_input = []
    for line in input:
        line_count += 1

        if line.split()[1] == 'cd' and line.split()[2] != '..':

            # Change input file to make all directories unique
            if line.split()[2] in dir_list:
                amended_input.append(line.strip() + '**' + str(line_count))

            else:
                amended_input.append(line.strip())

            dir_list.append(amended_input[-1].split()[2])
            dir_count += 1
        else:
            amended_input.append(line.strip())

    # For eaach directory in dir_list, creating a corresponding list of the directory size
    dir_size = []
    for dir in dir_list:
        
        in_dir_flag = False # To ensure we start at the correct point for the current directory
        file_path = [] # Track current position in directory
        current_size = 0 # Current size of working directory
        
        for line in amended_input:
            
            if line  == '$ cd ' + dir:
                in_dir_flag = True    
                
            if in_dir_flag:
                if line.split()[0] == '$': 

                            if line.split()[1] == 'cd' and line.split()[2] != '..': # Moving 'down'
                                file_path.append(line.split()[2])

                            elif line.split()[1] == 'cd' and file_path[-1] == dir: # Moving up outside current directory being calculated
                                break

                            elif line.split()[1] == 'cd' and file_path[-1] != dir: # Moving up but in sub directory of calculation
                                file_path.pop()

                # Ignore directory lines and sum the rest
                elif line.split()[0] == 'dir':
                    pass

                else:
                    current_size += int(line.split()[0])

        dir_size.append(current_size)

        # create dict of all directories (not necessary)
        dirs = {k:v for k,v in zip(dir_list,dir_size)}

        # root directory will contain all else so safe to assume this is all used space - alternative: max(dir_size)
        used_space = int(dirs['/'])
        
        # Device memory total =  70_000_000
        #  Update size = 30_000_000
        unused_space = 70_000_000 - used_space
        size_to_find = 30_000_000 - unused_space

        # Find the directories large enough to enable the update
        large_dirs = []
        for x in dir_size:
            if x >= size_to_find :
                large_dirs.append(x)

    return min(large_dirs)


print(part1())
print(part2())
