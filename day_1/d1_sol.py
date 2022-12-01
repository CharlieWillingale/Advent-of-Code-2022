with open('input.txt','r') as f:

    input = f.readlines()

# Lists (for simplicity) to hold each individual elf's caloric breakdown + overal elves. 
elves = []
elf_cals = []

for line in input:

    # Determine if a new elf list
    if len(line) > 1:

        elf_cals.append(line.strip())

    else:

        elves.append(elf_cals)
        elf_cals = []


total_cals_elf = []

# Part 1: Most calories

for elf in elves:

    cal_count = 0

    for snack in elf:

        cal_count += int(snack)
    
    total_cals_elf.append(cal_count)

print(max(total_cals_elf))

# Part 2: Sum of top 3

top_3 = sorted(total_cals_elf)[-3:]

cal_count = 0
for cals in top_3:

    cal_count += cals

print(cal_count)