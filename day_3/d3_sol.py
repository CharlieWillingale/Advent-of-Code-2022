import string

with open('input.txt','r') as f:

    inventory = f.readlines()
    backpacks = [x.strip() for x in inventory]


# part 1
def part_1() -> None:

    priority_list = {letter:str(index) for index, letter in enumerate(string.ascii_letters, start=1)}
    score = 0

    for pack in backpacks:

        pocket_1 = pack[:int(len(pack)/2)]
        pocket_2 = pack[int(len(pack)/2):]


        current_pack_comparison = []

        for item in pocket_1:
            
            current_pack_comparison.append(item) if (item in pocket_2 and item not in current_pack_comparison) else 'no match'

        for item in current_pack_comparison:

            score += int(priority_list[item])

    print(score)

# Part 2
def part_2() -> None:

    priority_list = {letter:str(index) for index, letter in enumerate(string.ascii_letters, start=1)}
    score = 0
    group_packs = []
    common_items = []

    for pack in range(0, len(backpacks)):
        
        group_packs.append(backpacks[pack])

        if len(group_packs) == 3:
            # Compare lists
            for item in group_packs[0]:

                if item in group_packs[1] and item in group_packs[2] and item not in common_items:

                    common_items.append(item)
                    score += int(priority_list[item]) 

            # reset lists
            group_packs = []
            common_items = []



    print(score)





            


part_1()
part_2()