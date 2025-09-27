# I'm gonna be a dead meat soon

grid_list = [' '] * 9
first_player = "X"
second_player = "O"
player_turn = first_player

def print_board():
    print(f" {grid_list[0]} | {grid_list[1]} | {grid_list[2]}")
    print("---+---+---")
    print(f" {grid_list[3]} | {grid_list[4]} | {grid_list[5]}")
    print("---+---+---")
    print(f" {grid_list[6]} | {grid_list[7]} | {grid_list[8]}")

def winner_check():
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for i in win_conditions:
        if grid_list[i[0]] == grid_list[i[1]] == grid_list[i[2]] != ' ':
            return grid_list[i[0]]  # return the symbol, not the variable
    return False

def draw_check():
    return ' ' not in grid_list

while True:
    print_board()
    try:
        chosen_box = int(input(f"\n{player_turn}'s turn! Choose a box (1-9): "))
        if 1 <= chosen_box <= 9 and grid_list[chosen_box-1] == ' ':
            grid_list[chosen_box-1] = player_turn
        else:
            print("Spot taken or invalid number. Try again.")
            continue
    except ValueError:
        print("Invalid input. Enter a number from 1 to 9.")
        continue

    winner = winner_check()
    if winner:
        print_board()
        print(f"\nCongratulations, {winner} won!")
        break

    if draw_check():
        print_board()
        print("\nIt's a draw!")
        break

    player_turn = second_player if player_turn == first_player else first_player
