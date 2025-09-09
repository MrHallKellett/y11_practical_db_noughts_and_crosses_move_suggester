CROSS = "❌"
NOUGHT = "🟢"
MAX_PLAYERS = 2
ROW_SIZE = 3
NUMBERS = "１	２	３	４	５	６	７	８	９".split("\t")

### Exemplar - use a database to log player moves in a game of noughts and crosses.
### allow the user to search for a recommended move.

def record_move():
    """record the most recent move in the database"""

###################################

def get_players():
    """get the players' names and record these in the database"""
    return []

###################################

def suggest_move():
    """suggest a move to the player"""

###################################

def get_move(board):
    """get the user to input a valid move on the board"""

    move_valid = False
    while not move_valid:
        print("Where to move?")
        position = input()

        if position.isdigit():
            position = int(position)
            if 0 <= position < ROW_SIZE ** 2:
                if board[position] in NUMBERS:  # space is unused
                    return position
                else:
                    print("That space is not free.")
            else:
                print("That wasn't a valid position.")
        else:
            print("That wasn't a valid number.")

    return position

###################################

def check_for_winner(board):
    """check if the game has been won"""

    for i in range(0, ROW_SIZE**2, ROW_SIZE):    
        if board[i] == board[i+1] == board[i+2]:
            return board[i]

    for i in range(ROW_SIZE):
        if board[i] == board[i+3] == board[i+6]:
            return board[i]
            
    if board[0] == board[4] == board[7]:
        return board[0]
    
    if board[2] == board[4] == board[6]:
        return board[2]



    return None

###################################

def display(board):
    """display the board"""

    for i in range(len(board)):        
        print(f"|{board[i]}", end="")
        if (i+1) % ROW_SIZE == 0:
            print("|")
            print("", "-" * ROW_SIZE * 3)

###################################

def add_to_grid(board, move, current_player):
    """add the current player's piece to the board"""

    if current_player == 1:
        piece = NOUGHT
    else:
        piece = CROSS

    board[move-1] = piece
    return board

###################################

def change_player(current_player):
    """switch to the next player"""

    print()

    current_player += 1
    if current_player > MAX_PLAYERS:
        current_player = 1

    print(f"It's now Player {current_player}'s turn")

    return current_player

###################################

def show_result(game_end):
    """show the result at the end of the game"""

    print()

    if game_end == "D":
        print("It was a draw")
    else:
        print(game_end, "was the winner.")

###################################

def main():

    current_player =  0
    game_end = False
    board = NUMBERS

    players = get_players()

    while not game_end:
        display(board)
        current_player = change_player(current_player)
        move = get_move(board)
        record_move()
        board = add_to_grid(board, move, current_player)
        game_end = check_for_winner(board)

    display(board)
    show_result(game_end)

###################################

if __name__ == "__main__":
    main()
