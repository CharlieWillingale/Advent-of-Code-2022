# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  Rules:
# 
#  a = rock (1pt), b = paper (2pt), c = scissors (3pt)
#  x = rock (1pt), y = paper (2pt), z = scissors (3pt)
#  draw = 3pt, win = 6pt, loss = 0pt
#
# ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# Load input for the games
with open('input.txt','r') as f:

    input = f.readlines()

def play_game(game_logic, input):

    game_total = 0

    for round in input:
        game_total += game_logic(round.strip().split(' '))

    return game_total

# Part 1:

def game_logic_1(game_round: list) -> int:

    score_card = {
        'X': 1,
        'Y': 2,
        'Z': 3,
        'W': 6,
        'D': 3,
        'L': 0
    }

    opponent_move = game_round[0]
    player_move = game_round[1]
    
    match opponent_move:

        case 'A':

            if player_move == 'X':

                outcome = 'D'

            elif player_move == 'Y':

                outcome = 'W'

            elif player_move == 'Z':

                outcome = 'L'

            else:

                raise Exception("Incorrect Player Input")

        case 'B':

            if player_move == 'X':

                outcome = 'L'

            elif player_move == 'Y':

                outcome = 'D'

            elif player_move == 'Z':

                outcome = 'W'

            else:

                raise Exception("Incorrect Player Input")
        case 'C':

            if player_move == 'X':

                outcome = 'W'

            elif player_move == 'Y':

                outcome = 'L'

            elif player_move == 'Z':

                outcome = 'D'

            else:

                raise Exception("Incorrect Player Input")

    return(score_card[outcome] + score_card[player_move])

print('Logic 1: ',play_game(game_logic_1,input))


#Part 2

def game_logic_2(game_round: list) -> int:

    score_card = {
        'A': 1,
        'B': 2,
        'C': 3,
        'Z': 6,
        'Y': 3,
        'X': 0
    }

    opponent_move = game_round[0]
    outcome = game_round[1]
    player_move = ''

    match outcome:

        case 'X':

            if opponent_move == 'A':

                player_move = 'C'

            elif opponent_move == 'B':

                player_move = 'A'

            elif opponent_move == 'C':

                player_move = 'B'

            else:

                raise Exception("Incorrect outcome")

        case 'Y':

            if opponent_move == 'A':

                player_move = 'A'

            elif opponent_move == 'B':

                player_move = 'B'

            elif opponent_move == 'C':

                player_move = 'C'

            else:

                raise Exception("Incorrect outcome")

        case 'Z':

            if opponent_move == 'A':

                player_move = 'B'

            elif opponent_move == 'B':

                player_move = 'C'

            elif opponent_move == 'C':

                player_move = 'A'

            else:

                raise Exception("Incorrect outcome")

        

    return(score_card[outcome] + score_card[player_move])

print('Logic 2: ',play_game(game_logic_2,input))
