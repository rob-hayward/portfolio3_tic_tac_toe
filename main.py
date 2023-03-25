import numpy as np
import random
from ascii import logo


# function that draws the playing board in the console.
# Takes a list as a parameter from which to populate board.
def grid_box(a_list):
    grid = f'╔═════╗  ╔═════╗  ╔═════╗\n' \
          f'║  {a_list[0]}  ║  ║  {a_list[1]}  ║  ║  {a_list[2]}  ║\n' \
          f'╚═════╝  ╚═════╝  ╚═════╝\n' \
           f'╔═════╗  ╔═════╗  ╔═════╗\n' \
          f'║  {a_list[3]}  ║  ║  {a_list[4]}  ║  ║  {a_list[5]}  ║\n' \
          f'╚═════╝  ╚═════╝  ╚═════╝\n' \
           f'╔═════╗  ╔═════╗  ╔═════╗\n' \
          f'║  {a_list[6]}  ║  ║  {a_list[7]}  ║  ║  {a_list[8]}  ║\n' \
          f'╚═════╝  ╚═════╝  ╚═════╝\n'
    print(grid)


# function that checks if player has 3 in a row.
def win_checker(a_list, player_name):
    # converts grid_list into a numpy array.
    grid_array = np.array(a_list)
    # shapes array into a 2D 3x3 grid
    grid_array = grid_array.reshape(3, 3)
    # ensures each row and column array is iterated over before exiting loop.
    for j in range(3):
        # makes array from each row and column.
        for i in range(3):
            row_array = grid_array[i, :]
            column_array = grid_array[:, i]
            # checks for win conditions by row, column and diagonal.
            if \
                    np.all(row_array == row_array[0]) or \
                    np.all(column_array == column_array[0]) or \
                    grid_array[0, 0] == grid_array[1, 1] == grid_array[2, 2] or \
                    grid_array[0, 2] == grid_array[1, 1] == grid_array[2, 0]:
                # if win condition met, prints the winner and ends game.
                print(f'Well done player {player_name} you have won!')
                return False
    # continues the game if there is no win condition.
    return True


def robo_go(a_list):
    valid_num = True
    while valid_num:
        robo_num = random.choice(a_list)
        if type(robo_num) == int:
            valid_num = False
            print(f'{player} chooses number {robo_num}.')
            return robo_num

    # except TypeError:
    #     robot_go(a_list)


# creates a list of numbers 1 to 9 to represent 9 squares on tic,tac, toe board
grid_list = []
for n in range(9):
    grid_list.append(n+1)

# logo
print(logo)

# player instructions.
print('Welcome to the classic game of tic-tac-toe.\n'
      'Play against a friend or Robo.XO, an A.I. tic-tac-toe foe!\n'
      'Take turns to place your "X" or "O" mark in one of the boxes marked 1 to 9.\n'
      'If you manage to place 3 of your marks in a row (vertically, horizontally or diagonally) then you win!')

players = int(input('\nHow many players are there? Enter 1 or 2: '))

grid_box(grid_list)

# sets game to on and turn 1.
game_on = True
turn = 1

while game_on:
    if players == 1 and turn % 2 == 0:
        mark = 'O'
        player = 'Robo.XO'
        num = robo_go(grid_list)
    elif players == 2 and turn % 2 == 0:
        mark = 'O'
        player = 2
        num = int(input(f'Player {player}, choose an available number between 1-9:'))
    else:
        mark = 'X'
        player = 1
        num = int(input(f'Player {player}, choose an available number between 1-9:'))
    if num not in grid_list:
        print(f'Sorry player {player}, that number is not available, please try again.')
    else:
        grid_list[num-1] = mark
        grid_box(grid_list)
        game_on = win_checker(grid_list, player)
        turn += 1
        if turn > 9:
            game_on = False


# if players == 1 and turn % 2 == 0:
#     mark = 'O'
#     player = 'Robot.XO'
#     num = random.randint(1, 9) in grid_list