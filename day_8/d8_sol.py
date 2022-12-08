from utils import read_input

# Load input
input = read_input('./input.txt')

#
# Part 1 solution
#

def part1():

    num_rows = len(input)
    num_cols = len(input[0].strip())

    visible_count = 0
    # Loop over the rows and columns in the grid
    for r in range(0,num_rows):
        for c in range(0,num_cols):

            tree_height = int(input[r][c])

            visible_flag = False

            # check if outside tree
            if r == 0 or c == 0 or r == num_rows -1 or c == num_cols -1:
                    visible_flag = True
            else:
                # check positive direction in grid for height differences
                # check current row
                for i in range(c+1,num_cols):
                    if i == (num_cols - 1) and int(input[r][i]) < tree_height:
                        visible_flag = True
                        break

                    elif int(input[r][i]) < tree_height:
                        pass

                    else:
                        break
                
                # check current column
                for i in range(r+1,num_rows):
                    if i == (num_cols - 1) and int(input[i][c]) < tree_height:
                        visible_flag = True
                        break

                    elif int(input[i][c]) < tree_height:
                        pass

                    else:
                        break

                # check negative direction in grid for height differences
                # check current row
                for i in range(c-1,-1,-1):
                    if i == 0 and int(input[r][i]) < tree_height:
                        visible_flag = True
                        break

                    elif int(input[r][i]) < tree_height:
                        pass

                    else:
                        break
                
                # check current column
                for i in range(r-1,-1,-1):
                    if i == 0 and int(input[i][c]) < tree_height:
                        visible_flag = True
                        break

                    elif int(input[i][c]) < tree_height:
                        pass

                    else:
                        break

            if visible_flag: 
                visible_count += 1

    return(visible_count)


#
# Part 1 solution
#

def part2():

    num_rows = len(input)
    num_cols = len(input[0].strip())

    scenic_score = 0
    # Loop over the rows and columns in the grid
    for r in range(0,num_rows):
        for c in range(0,num_cols):

            tree_height = int(input[r][c])

            view_distance = [0,0,0,0]


            if r == 0 or c == 0 or r == num_rows -1 or c == num_cols -1:
                pass
            
            else:
                # check positive direction in grid for height differences and add to score
                # check current row
                for i in range(c+1,num_cols):

                    if int(input[r][i]) < tree_height:
                        view_distance[0] += 1

                    else:
                        view_distance[0] += 1
                        break
                
                # check current column
                for i in range(r+1,num_rows):
                    
                    if int(input[i][c]) < tree_height:
                        view_distance[1] += 1

                    else:
                        view_distance[1] += 1
                        break


                # check negative direction in grid for height differences
                # check current row
                for i in range(c-1,-1,-1):

                    if int(input[r][i]) < tree_height:
                        view_distance[2] += 1

                    else:
                        view_distance[2] += 1
                        break
                
                # check current column
                for i in range(r-1,-1,-1):

                    if int(input[i][c]) < tree_height:
                        view_distance[3] += 1

                    else:
                        view_distance[3] += 1
                        break

                current_scenic_score = view_distance[0]*view_distance[1]*view_distance[2]*view_distance[3]
                if current_scenic_score > scenic_score:
                    scenic_score = current_scenic_score

    return(scenic_score)



print(part1())
print(part2())
