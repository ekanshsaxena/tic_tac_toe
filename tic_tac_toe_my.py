import random
game_input=[' ','X','O','X','O','X','O','X','O','X']
def board(game_input):
    print(game_input[7] + '|' + game_input[8] + '|' + game_input[9])
    print(game_input[4] + '|' + game_input[5] + '|' + game_input[6])
    print(game_input[1] + '|' + game_input[2] + '|' + game_input[3])

#board(game_input)

def choose_marker():
    a=' '
    whom=random.randint(1,2)
    while a != 'X' or a != 'O':
            a = input("Player {} choose your marker ('X'/'O'): ".format(whom))
            if a == 'X':
                return [whom,'X', 'O']
            elif (a == 'O'):
                return [whom,'O', 'X']
            else:
                continue


def win(game_input, marker):
    return ((game_input[1] == game_input[2] == game_input[3] == marker) or
            (game_input[4] == game_input[5] == game_input[6] == marker) or
            (game_input[7] == game_input[8] == game_input[9] == marker) or
            (game_input[7] == game_input[5] == game_input[3] == marker) or
            (game_input[1] == game_input[5] == game_input[9] == marker) or
            (game_input[1] == game_input[4] == game_input[4] == marker) or
            (game_input[2] == game_input[5] == game_input[8] == marker) or
            (game_input[3] == game_input[6] == game_input[9] == marker))

def check(game_input):
    if (game_input[1] != ' ' and game_input[2] != ' ' and game_input[3] != ' ' and game_input[4] != ' ' and game_input[5] != ' ' and game_input[6] != ' ' and game_input[7] != ' ' and game_input[8] != ' ' and game_input[9] != ' ' ):
        return False
    else:
        return True

def give_markers(input_marker):
    global player_1_marker
    global player_2_marker
    if input_marker[0] == 1:
        player_1_marker = input_marker[1]
        player_2_marker = input_marker[2]
    else:
        player_2_marker = input_marker[1]
        player_1_marker = input_marker[2]
    print("Player 1, Your marker is " + player_1_marker + "\n" + "Player 2, Your marker is " + player_2_marker)

def take_position(game_input,player_choice):
    board(game_input)
    position = 0
    while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or game_input[int(position)] != ' ':
        position = input("Player {}, choose your position from NumPad: ".format(player_choice))

    return position

def put_marker(game_input,position,player_marker):
    game_input[position]=player_marker
while True:
    inputs=[' ']*10
    print('{:*^50}'.format("TIC_TAC_TOE"))
    input_marker = []
    input_marker = choose_marker()
    give_markers(input_marker)
    player_choice = random.randint(1, 2)
    ready=0
    while ready != 'Y' or ready != 'N':
            ready=input("Are You Ready To Play The Game(Y/N):  ")
            if ready == 'N':
                  game_on=False
                  break
            elif ready=='Y':
                game_on=True
                break
            else:
                 continue
    while game_on:
        if player_choice==1:
            position = int(take_position(inputs, player_choice))
            put_marker(inputs,position,player_1_marker)
            if win(inputs, player_1_marker):
                board(inputs)
                print('{:*^50}'.format("Yippe!!! Player 1 won the game."))
                game_on=False
            else:
                if check(inputs):
                    player_choice=2
                else:
                    print('{:*^50}'.format("Game Tied"))
                    game_on=False
        else:
            position = int(take_position(inputs, player_choice))
            put_marker(inputs, position, player_2_marker)
            if win(inputs, player_2_marker):
                board(inputs)
                print('{:*^50}'.format("Yippe!!! Player 2 won the game."))
                game_on=False
            else:
                if check(inputs):
                    player_choice = 1
                else:
                    print('{:*^50}'.format("Game Tied"))
                    game_on = False
    play_again = input("Do You Want To Play Again(Y/N): ")
    if play_again == 'Y':
                continue
    else:
         exit()