import time
from itertools import groupby
# Runtime: 

# Elves have been assigned areas to clean. Many of them have been assigned to clean the same areas, they are interested in
# reducing duplication of effort.
# They have paired up.
# Each area assignment is in the format 6-9, which means areas 6, 7, 8, 9 have been assigned to that elf.
# Each row of data has 2 area assignments seperated by a comma, this represents the elf pair.

# Question 1:
# How many elf pairs have 1 area assignment that completely overlaps the other?

# This is for timing run time
start_time = time.time()

# This is for timing run time
start_time = time.time()

# Read the file into a variable
my_file = open('./Input.txt', 'r')

# reading the file
data = my_file.read()

# Splitting the text 
# when newline ('\n') is seen.
data_into_list = data.split("\n")

#print(data_into_list)
my_file.close()

# Use the comma delimiter to split the list into elf1 and elf2.
# Then use the hyphen delimter to find min & max areaID for each elf.
# Count intstances where:
# min(elf1AreaID_Low) < min(elf2AreaID_Low) and max(elf1AreaID_High) > max(elf2AreaID_High) or min(elf1AreaID_Low) > min(elf2AreaID_Low) and max(elf1AreaID_High) < max(elf2AreaID_High)

# Didn't understand groupby.
# chunks = (list(g) for k,g in groupby(data_into_list, key=lambda x: x != ',') if k)
# for chunk in chunks:    
#     ...
# print(chunk)

# data_into_list = data_into_list[0:4] 

# Split each element in list
Elf1 = [item.split(',', 1)[0] for item in data_into_list]
Elf2 = [item.split(',', 1)[1] for item in data_into_list]

# Make a seperate list for the min & max areaID for elf 1 & 2.
Elf1AreaID_Low = [item.split('-', 1)[0] for item in Elf1]
Elf1AreaID_High = [item.split('-', 1)[1] for item in Elf1]
Elf2AreaID_Low = [item.split('-', 1)[0] for item in Elf2]
Elf2AreaID_High = [item.split('-', 1)[1] for item in Elf2]

i = 0
Instances = 0
while i < len(data_into_list):
    if (int(Elf1AreaID_Low[i]) <= int(Elf2AreaID_Low[i]) and int(Elf1AreaID_High[i]) >= int(Elf2AreaID_High[i])) or (int(Elf2AreaID_Low[i]) <= int(Elf1AreaID_Low[i]) and int(Elf2AreaID_High[i]) >= int(Elf1AreaID_High[i])):
        Instances += 1
        i += 1
        # '72-92,48-88'
        # print(Elf1AreaID_Low[i])
        # print(Elf1AreaID_High[i])
        # print(Elf2AreaID_Low[i])
        # print(Elf2AreaID_High[i])
    else:
        i += 1
# print(data_into_list)

# print(Elf1)
# print(Elf2)

# print(Elf1AreaID_Low)
# print(Elf1AreaID_High)
# print(Elf2AreaID_Low)
# print(Elf2AreaID_High)

# print(Instances)

answer  = Instances
# answer2 = ''

# print('Answer to part 1:', answer)
# print('Answer to part 2:', answer2)

# print("--- %s seconds ---" % (time.time() - start_time))