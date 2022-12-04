with open('input.txt','r') as f:

    input = f.readlines()
    

def part_1():

    assignments = [x.strip().split(',') for x in input]
    overlap_count = 0

    for pair in assignments:

        elf_1_lower,elf_1_upper = pair[0].split('-')
        elf_2_lower,elf_2_upper = pair[1].split('-')

        if int(elf_1_lower) >= int(elf_2_lower) and int(elf_1_lower) <= int(elf_2_upper) and int(elf_1_upper) <= int(elf_2_upper) or int(elf_2_lower) >= int(elf_1_lower) and int(elf_2_lower) <= int(elf_1_upper) and int(elf_2_upper) <= int(elf_1_upper):

            overlap_count += 1
        
    print(overlap_count)

def part_2():

    assignments = [x.strip().split(',') for x in input]
    overlap_count = 0

    for pair in assignments:

        elf_1_lower,elf_1_upper = pair[0].split('-')
        elf_2_lower,elf_2_upper = pair[1].split('-')

        for elf_1 in range(int(elf_1_lower), int(elf_1_upper) +1):

            if elf_1 in range(int(elf_2_lower), int(elf_2_upper) + 1):

                overlap_count += 1 
                break
        
    print(overlap_count)


part_1()
part_2()