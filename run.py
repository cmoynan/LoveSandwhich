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


def print_board(board):
    """
    Print the game board.
    """
    print("   " + " ".join(str(i) for i in range(BOARD_SIZE)))
    print("  " + "--" * BOARD_SIZE)
    for i in range(BOARD_SIZE):
        print(f"{i} | {' '.join(board[i])}")


def get_guess():
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


def play_game():
    """
    Main game loop.
    """
    print("Welcome to Battleship!")

    # Initialize game board
    board = initialize_board()
    place_ships(board)
    print_board(board)

    # Game loop
    while True:
        print("Take a guess:")
        row, col = get_guess()

        # Check guess result
        if board[row][col] == SHIP:
            print("Hit!")
            board[row][col] = HIT
        else:
            print("Miss!")
            board[row][col] = MISS

        print_board(board)

        # Check for game over
        if all(EMPTY not in row for row in board):
            print("Congratulations! You sunk all the battleships!")
            break


if __name__ == "__main__":
    play_game()