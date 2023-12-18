import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_win(turn: str, board: dict) -> None:
    clear_screen()
    print_board(board)
    print("\n      Game Over \n")
    print(f" **** Player {turn} has won ! \n\n")

def print_board(board):
    print()
    print ("\t" + board['7'] + '|' +board['8'] + '|' + board['9'])
    print ("\t" + "-+-+-")
    print ("\t" + board['4'] + '|' +board['5'] + '|' + board['6'])
    print ("\t" + "-+-+-")
    print ("\t" + board['1'] + '|' +board['2'] + '|' + board['3'])
    print()
    

def check_win(turn: str, board: dict) -> bool:
    # Check rows
    for row in range(3):
        if board[f'{row * 3 + 1}'] == board[f'{row * 3 + 2}'] == board[f'{row * 3 + 3}'] == turn and board[f'{row * 3 + 1}'] != ' ':
            print_win(turn, board)
            return True

    # Check columns
    for col in range(3):
        if board[f'{col + 1}'] == board[f'{col + 4}'] == board[f'{col + 7}'] == turn and board[f'{col + 1}'] != ' ':
            print_win(turn, board)
            return True

    # Check diagonals
    if (board['1'] == board['5'] == board['9'] == turn and board['1'] != ' ') or \
       (board['3'] == board['5'] == board['7'] == turn and board['3'] != ' '):
        print_win(turn, board)
        return True

    return False
    

def is_move_valid(move: str, board: dict) -> bool:
    return move in board and board[move] == ' '


def get_valid_move(board: dict) -> str:
    while True:
        move = input("Where do you want to go? : ")
        if is_move_valid(move, board):
            return move
        else:
            print("Invalid move. Please try again.")


def prompt_restart():
    return input("Do you want to play again? (y)es or (n)o: ").lower() == "y"

def main():
    while True:
        the_board = {
            '7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' ',
        }

        board_keys = list(the_board.keys())

        turn = "X"
        count = 0

        for _ in range(9):  # Change to 9 to match the number of moves
            clear_screen()
            print_board(the_board)
            print(f"It's Player {turn}'s turn")

            move = get_valid_move(the_board)

            the_board[move] = turn
            count += 1

            if count >= 5:
                win = check_win(turn, the_board)
                if win:
                    print_win(turn, the_board)
                    break  # Exit the loop on win

            if count == 9:
                print("Game Over !")
                print("It's a tie")
                break  # Exit the loop on tie

            turn = "O" if turn == "X" else "X"

            #input("Press Enter to continue...")  # Pause until Enter is pressed

        if not prompt_restart():
            break  # Exit the outer loop on 'n' or invalid input

if __name__ == "__main__":
    main()