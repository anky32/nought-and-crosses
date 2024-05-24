import random
import os.path
import json
import os


def draw_board(board):
# develop code to draw the board

    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))

def welcome(board):
    # prints the welcome message

    print("Welcome to the Unbeatable Noughts and Crosses game.")
    print("The board layout is shown below:")
    board = [1,2,3,4,5,6,7,8,9]

    # display the board by calling draw_board(board)
    draw_board(board)

def initialise_board(board):
    # develop code to set all elements of the board to one space ' '

    for i in range(9):
        board.append(" ")
    return board

def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,

    while True:
        try:
            move = int(input("Your move (1-9): ").strip())
            if move not in range(1, 10):
                print("Invalid number. Please choose a number between 1 and 9.")
            elif board[move - 1] != ' ':
                print("That space is already taken. Please choose another.")
            else:
                board[move - 1] = 'X'

                # and return move
                return move
        except ValueError:
            print("Invalid input. Please enter a number.")

def choose_computer_move(board):
    #code to let the computer chose a cell to put a nought in

    print("Computer move")
    valid_moves = [i + 1 for i in range(9) if board[i] == " "]
    move = random.choice(valid_moves) 
    board[move - 1] = 'O'

    # return move
    return move

def check_for_win(board, mark):
    #check if either the player or the computer has won

    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == mark:

            # return True if someone won, False otherwise
            return True
    return False

def check_for_draw(board):
# develop code to check if all cells are occupied

    return not " " in board

def play_game(board):
    # develops the code to play the game
    
    board = []
    welcome(board)
    initialise_board(board)
    while True:
        get_player_move(board)
        draw_board(board)
        if check_for_win(board, 'X'):
            return 1
        elif check_for_draw(board):
            return 0
        choose_computer_move(board)
        draw_board(board)
        if check_for_win(board, 'O'):
            return -1
        elif check_for_draw(board):
            return 0
        
def menu():
    # This function displays a menu of options and prompts the user to enter a choice.

    print("Enter one of the following options.")
    print("1 - Play the game")
    print("2 - Save score in file 'leaderboard.txt'")
    print("3 - Load and display the scores from the 'leaderboard.txt'")
    print("q - End the program")
    while True:
        try:
            choice = input("Enter your choice: ").strip().lower()
            if choice not in ['1', '2', '3', 'q']:
                raise ValueError("Invalid choice. Please enter '1', '2', '3', or 'q'.")
            return choice
        except ValueError as e:
            print(e)

def load_scores():
    #load the leaderboard scores from the file leaderboard.txt with the player name and score

    if os.path.exists("leaderboard.txt"):
        
        with open("leaderboard.txt", "r") as file:
            return json.load(file)
    else:
       
        return {}

def save_score(score):
   #ask the player for their name and save to leaderboard.txt
    player_name = input("Enter your name: ")
    leaderboard = load_scores()
    leaderboard[player_name] = score
    with open("leaderboard.txt", "w") as file:
        json.dump(leaderboard, file)

def display_leaderboard(leaderboard):
    # display the leaderboard scores

    print("Leaderboard:")
    for name, score in leaderboard.items():
        print("{}: {}".format(name, score))


