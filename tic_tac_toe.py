

tiles = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
player = -1


def print_grid(board):
    for row in board:
        print("|", end="")
        for tile in row:
            if tile == 0:
                tile = "_"
            if tile == 1:
                tile = "x"
            if tile == 2:
                tile = "o"
            print(f"{tile}|", end="")
        print()


def game_quit(u_input):
    if u_input == "q":
        return True
    else:
        return False


def check_correct(u_input):
    if len(u_input) == 2 and u_input.isnumeric():
        row = int(u_input[0]) - 1
        column = int(u_input[1]) - 1
        print(len(u_input))
        if row not in [0, 1, 2] or column not in [0, 1, 2]:
            print("Incorrect choice.")
            return False
        else:
            # correct choice (row and column)
            if tiles[row][column] == 0:
                print(tiles[row][column])
                if player == -1:
                    tiles[row][column] = 1
                elif player == 1:
                    tiles[row][column] = 2
                return True
            else:
                return False
    else:
        print("Incorrect choice.")
        print(len(u_input))
        return False


def win_message():
    if player == -1:
        print(f'Player "X" won!')
    elif player == 1:
        print(f'Player "O" won!')


def win_conditions():
    status = False
    for player_number in range(1, 3):
        print(player_number)
        for n in range(3):
            if tiles[n][0] == tiles[n][1] == tiles[n][2] == player_number:
                win_message()
                status = True
            if tiles[0][n] == tiles[1][n] == tiles[2][n] == player_number:
                win_message()
                status = True
        print(player_number)
        if tiles[0][0] == tiles[1][1] == tiles[2][2] == player_number:
            win_message()
            status = True
        if tiles[0][2] == tiles[1][1] == tiles[2][0] == player_number:
            win_message()
            status = True
    return status


game_run = True
while game_run:
    print(tiles)
    print("======================================")
    if player == -1:
        print(f'It is player "X" turn.')
    else:
        print(f'It is player "O" turn.')
    print_grid(tiles)
    choice = input('Choose a tile as an example "22", where first is a row and second is a column.\n'
                   'If you want to quit, type "q".\n'
                   'Your choice: ')
    if game_quit(choice):
        game_run = False

    if not check_correct(choice):
        print("not correct")
        continue

    if win_conditions():
        game_run = False
        print_grid(tiles)
        print("Thank you for playing!")
    else:
        player *= -1
