# This is a tic tac toe game.
# Importing modules
import random

# Defining players.
player_1 = 'X'
player_2 = 'O'

# function to generate a dummy board to explain the location of cell to the user.


def render_dummy_board():
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    first_row = f'{board[0][0]} | {board[0][1]} | {board[0][2]}\n'
    second_row = f'{board[1][0]} | {board[1][1]} | {board[1][2]}\n'
    third_row = f'{board[2][0]} | {board[2][1]} | {board[2][2]}\n'

    # Create new combined string with rows
    lines = f'{first_row}{second_row}{third_row}'
    print(lines)

# function to generate an empty board.


def empty_board():
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    return board

# Defining a function to create a dictionary refrencing to each cell in the board.


def dictionary():
    dictionary = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2)
    }
    return dictionary

# Define empty_cell
empty_cell = '-'


def render(board):
    first_row = f'{board[0][0]} | {board[0][1]} | {board[0][2]}\n'
    second_row = f'{board[1][0]} | {board[1][1]} | {board[1][2]}\n'
    third_row = f'{board[2][0]} | {board[2][1]} | {board[2][2]}\n'

    # Create new combined string with rows
    lines = f'{first_row}{second_row}{third_row}'
    # Separate rows by a line of hyphens
    print(lines.replace('None', empty_cell))
 # type: ignore

# Defining function to input coordinates from user.


def input_coordinates():
    # Inputting cell number from user.
    usr_input = input("Enter the cell:")
    # Checking if the input is not empty and in range.
    while usr_input.isdigit() == False or int(usr_input) not in range(1, 10):
        print("Invalid input. Try again")
        usr_input = (input("Enter the cell:"))
    usr_input = int(usr_input)
    # Creating a dictionary to map cell number to coordinates.
    cell_dict = dictionary()
    # Returning the coordinates of the cell.
    move_coordinates = cell_dict[usr_input]
    return move_coordinates

# Make a move in the given gameboard based on player's coordinates


def make_move(old_board, move_coordinates, player_move):

    # Create a duplicate gameboard for the new board
    new_board = old_board

    # Modify the new board with player's move
    new_board[move_coordinates[0]][move_coordinates[1]] = player_move

    # Return the modified board
    return new_board


# Check if the board is full.
def is_full(board):
    for row in board:
        for box in row:
            if box == None:
                return False
    return True

# Check for winner.


def winner(board):
    # Check for horizontal wins
    for row in board:
        if row[0] == row[1] == row[2] != None:
            return row[0]
    # Check for vertical wins
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != None:
            return board[0][column]
    # Check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]
    # Check for tie
    if is_full(board):
        return 'Tie'
    # No winner
    return None

# Defining function to play the game.


def play_game():
    # Print the dummy board.
    render_dummy_board()
    print("Enter the cell number according to above board.\n")
    # Generate an empty board.
    board = empty_board()
    # Print the empty board.
    render(board)
    # Randomly choose who goes first.
    turn = random.choice([player_1, player_2])
    print(turn, "goes first")
    # Keep playing until there is a winner.
    while winner(board) == None:
        # If it is player 1's turn
        if turn == player_1:
            # Take input from player 1.
            move_coordinates = input_coordinates()
            # Checking if the box is already taken.
            if board[move_coordinates[0]][move_coordinates[1]] != None:
                print("This move is not possible. The box is already taken. Try again")
                move_coordinates = input_coordinates()
            # Update the board with player 1's move.
            board = make_move(board, move_coordinates, player_1)
            # Print the updated board.
            render(board)
            # Change the turn to player 2.
            turn = player_2
            # Print whose turn it is.
            print("It is", turn, "'s turn")
        # If it is player 2's turn.
        else:
            # Take input from player 2.
            move_coordinates = input_coordinates()
            # Checking if the box is already taken.
            if board[move_coordinates[0]][move_coordinates[1]] != None:
                print("This move is not possible. The box is already taken. Try again")
                move_coordinates = input_coordinates()
            # Update the board with player 2's move.
            board = make_move(board, move_coordinates, player_2)
            # Print the updated board.
            render(board)
            # Change the turn to player 1.
            turn = player_1
            # Print whose turn it is.
            print("It is", turn, "'s turn")
    # Print the winner.
    if winner(board) == 'X' or winner(board) == 'O':
        print("The winner is:", winner(board))
    elif winner(board) == 'Tie':
        print("It is a tie.")    
    # Ask the players if they want to play again.
    play_again = input("Do you want to play again? (y/n)")
    # If yes, play again.
    if play_again == 'y':
        play_game()
    # If no, exit the program.
    else:
        exit()


# Call the play_game function to start the game.
play_game()
