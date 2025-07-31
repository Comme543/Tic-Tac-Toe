import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("🎮 Tic Tac Toe")
        self.window.configure(bg="#282c34")
        self.window.resizable(False, False)

        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        self.title_label = tk.Label(self.window, text="Tic Tac Toe", font=("Comic Sans MS", 24, "bold"),
                                    bg="#282c34", fg="#61dafb", pady=10)
        self.title_label.grid(row=0, column=0, columnspan=3)

        self.create_buttons()
        self.window.mainloop()

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.window, text="", font=("Comic Sans MS", 36, "bold"),
                               width=5, height=2,
                               bg="#1e1e1e", fg="#ffffff", activebackground="#44475a",
                               command=lambda i=i: self.on_click(i))
            button.grid(row=(i // 3) + 1, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

    def on_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player,
                                       fg="#d46262" if self.current_player == "X" else "#61a93a")

            if self.check_winner(self.current_player):
                self.highlight_winner(self.current_player)
                messagebox.showinfo("🏆 Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("🤝 Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        self.winning_combo = []
        win_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in win_positions:
            if all(self.board[pos] == player for pos in combo):
                self.winning_combo = combo
                return True
        return False

    def highlight_winner(self, player):
        for index in self.winning_combo:
            self.buttons[index].config(bg="#d1d691", fg="#000000")

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="", bg="#1e1e1e", fg="#ffffff")

if __name__ == "__main__":
    TicTacToe()
