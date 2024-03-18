import random

# Constants
BOARD_SIZE = 5
NUM_SHIPS = 3
EMPTY = " "
SHIP = "O"
HIT = "X"
MISS = "-"


def initialize_board():
    """
    Initialize an empty game board.
    """
    return [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]


def place_ships(board):
    """
    Randomly place ships on the game board.
    """
    for _ in range(NUM_SHIPS):
        row = random.randint(0, BOARD_SIZE - 1)
        col = random.randint(0, BOARD_SIZE - 1)
        board[row][col] = SHIP


def print_board(player_board, computer_board):
    """
    Print the player's board and the computer's board with missed shots revealed.
    """
    print("   " + " ".join(str(i) for i in range(BOARD_SIZE)) + "       " + " ".join(str(i) for i in range(BOARD_SIZE)))
    print("  " + "--" * BOARD_SIZE + "      " + "--" * BOARD_SIZE)
    for i in range(BOARD_SIZE):
        print(f"{i} | {' '.join(player_board[i])}      {' '.join(computer_board[i])}")

def get_player_guess():
    """
    Get the player's guess for row and column.
    """
    while True:
        try:
            row = int(input("Enter row (0-4): "))
            col = int(input("Enter column (0-4): "))
            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                return row, col
            else:
                print("Invalid input! Please enter numbers between 0 and 4.")
        except ValueError:
            print("Invalid input! Please enter valid integers.")


def get_computer_guess():
    """
    Generate a random guess for the computer.
    """
    row = random.randint(0, BOARD_SIZE - 1)
    col = random.randint(0, BOARD_SIZE - 1)
    return row, col


def play_game():
    """
    Main game loop.
    """
    print("Welcome to Battleship!")

    # Initialize player and computer boards
    player_board = initialize_board()
    computer_board = initialize_board()
    place_ships(player_board)
    place_ships(computer_board)

    # Game loop
    while True:
        # Player's turn
        print("Player's turn:")
        print_board(player_board, computer_board)
        player_row, player_col = get_player_guess()

        if computer_board[player_row][player_col] == SHIP:
            print("Hit!")
            computer_board[player_row][player_col] = HIT
        else:
            print("Miss!")
            computer_board[player_row][player_col] = MISS

        # Check for player win
        if check_game_over(computer_board):
            print("Congratulations! You sunk all the computer's battleships!")
            break

        # Computer's turn
        print("\nComputer's turn:")
        computer_row, computer_col = get_computer_guess()

        if player_board[computer_row][computer_col] == SHIP:
            print("Computer hit your battleship!")
            player_board[computer_row][computer_col] = HIT
        else:
            print("Computer missed!")
            player_board[computer_row][computer_col] = MISS

        # Check for computer win
        if check_game_over(player_board):
            print("Oops! The computer sunk all your battleships. Better luck next time!")
            break


if __name__ == "__main__":
    play_game()