# print tic-tac-toe board on screen
def print_board(board):
    print(" " + board["top_l"] + " | " + board["top_m"] + " | " +
          board["top_r"] + " ")
    print("---+---+---")
    print(" " + board["mid_l"] + " | " + board["mid_m"] + " | " +
          board["mid_r"] + " ")
    print("---+---+---")
    print(" " + board["bot_l"] + " | " + board["bot_m"] + " | " +
          board["bot_r"] + " ")


# create function to check the winner
def win_check(move: str) -> bool:
    """
    function to check either `o` or `x` win the game, by checking all horizontal, vertical and diagonal line

    :param move: insert `x` to check win status for x and vice versa
    :return: will return true to indicate that the player wins the game if meets any of the condition
    """
    top = (move_spaces["top_l"] == move and move_spaces["top_m"] == move and move_spaces["top_r"] == move)
    mid = (move_spaces["mid_l"] == move and move_spaces["mid_m"] == move and move_spaces["mid_r"] == move)
    bot = (move_spaces["bot_l"] == move and move_spaces["bot_m"] == move and move_spaces["bot_r"] == move)
    left_ver = (move_spaces["top_l"] == move and move_spaces["mid_l"] == move and move_spaces["bot_l"] == move)
    mid_ver = (move_spaces["top_m"] == move and move_spaces["mid_m"] == move and move_spaces["bot_m"] == move)
    right_ver = (move_spaces["top_r"] == move and move_spaces["mid_r"] == move and move_spaces["bot_r"] == move)
    ltr_dia = (move_spaces["top_l"] == move and move_spaces["mid_m"] == move and move_spaces["bot_r"] == move)
    rtl_dia = (move_spaces["top_r"] == move and move_spaces["mid_m"] == move and move_spaces["bot_l"] == move)
    if top or mid or bot or left_ver or mid_ver or right_ver or ltr_dia or rtl_dia:
        return True


# create function for the game
def game():
    """
    Start the tic-tac-toe game
    """
    print("Press ENTER to start")
    input()

    turn = "x"
    # print all available moves every time the player takes turn
    while True:
        available_moves = []
        print_board(move_spaces)
        print("{} turn to move. Which move? ".format(turn))
        print("Available moves:")
        for boards, moves in move_spaces.items():
            if moves == " ":
                available_moves.append(boards)

        print(", ".join(available_moves))

        # take input as player moves, print invalid if moves not available
        player_move = input()
        if player_move.casefold() in available_moves:
            move_spaces[player_move.casefold()] = turn
        else:
            print("Invalid moves")
            continue

        # change side every time player makes a move
        if turn == "x":
            turn = "o"
        else:
            turn = "x"

        # check winner using earlier function
        if win_check("x"):
            print_board(move_spaces)
            print("X player win!")
            break
        elif win_check("o"):
            print_board(move_spaces)
            print("O player win!")
            break
        elif len(available_moves) == 1:
            print("There's no winner")
            break


# start the game in loop
while True:
    # reset move spaces everytime new game start
    move_spaces = {"top_l": " ", "top_m": " ", "top_r": " ",
                   "mid_l": " ", "mid_m": " ", "mid_r": " ",
                   "bot_l": " ", "bot_m": " ", "bot_r": " "}

    game()

    # ask player either they want to restart the game
    restart = input("Play again? Y for yes, any key to exit\n")
    if restart.casefold() == "y":
        continue
    else:
        break
