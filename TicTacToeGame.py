import time
import tkinter as tk
import random


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return ""


def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True


def computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]
    return random.choice(empty_cells)


def on_click(row, col, board, buttons, winner_label):
    if board[row][col] == "" and not winner_label.cget("text"):
        board[row][col] = "X"
        buttons[row][col].config(text="X", state="disabled")
        winner = check_winner(board)
        if winner:
            winner_label.config(text=f"Player {winner} wins!")
            return

        if not is_board_full(board):
            computer_row, computer_col = computer_move(board)
            board[computer_row][computer_col] = "O"
            buttons[computer_row][computer_col].config(text="O", state="disabled")

            winner = check_winner(board)
            if winner:
                winner_label.config(text=f"Computer {winner} wins!")

        else:
            winner_label.config(text="Draw!")


def create_board():
    board_window = tk.Tk()
    board_window.title("Tic-Tac-Toe")

    buttons = []
    for i in range(3):
        row_buttons = []
        for j in range(3):
            button = tk.Button(board_window, width=10, height=5, command=lambda row=i, col=j: on_click(row, col, board, buttons, winner_label))
            button.grid(row=i, column=j)
            button.config(font=("Helvetica", 12, "bold"))
            row_buttons.append(button)
        buttons.append(row_buttons)

    winner_label = tk.Label(board_window, text="", font=("Helvetica", 14, "bold"))
    winner_label.grid(row=3, columnspan=3)

    return board_window, buttons, winner_label

if __name__ == "__main__":
    board_window, buttons, winner_label = create_board()
    board = [["" for _ in range(3)] for _ in range(3)]
    board_window.mainloop()


