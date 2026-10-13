# Write code for tic tac toe
# 1. Create a 3x3 board
# 2. Take input from player 1 and player 2
# 3. Check if the input is valid
# 4. Check if the game is over
# 5. Check if the game is a draw
# 6. Check if the game is won
# 7. Print the board after each move
# 8. Print the winner
# 9. Print the draw message
# 10. Print the invalid input message
# 11. Print the game over message

def greet():
    # greet the user 
    print("Good morning! Welcome to Tic Tac Toe!")
    print("Player 1 is X")
    print("Player 2 is O")
    print("Let's start the game!")



def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all([cell != " " for row in board for cell in row])

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        row = int(input(f"Player {current_player}, enter the row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter the column (0, 1, 2): "))

        if row not in range(3) or col not in range(3) or board[row][col] != " ":
            print("Invalid input, please try again.")
            continue

        board[row][col] = current_player


        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        elif check_draw(board):
            print_board(board)
            print("The game is a draw!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()