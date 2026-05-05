

# tic tac toe game 

import tkinter as tk #this is a GUI library for this game 
from tkinter import messagebox   #this tool is for the messages and pops for announcement of winner , loser or draw 

# ---------------- GAME SETUP ----------------
window = tk.Tk()   #Tk is used from tk library , it is used to create a window without this GUI can not appear , so this window shows us that 
# it basically , initializes the GUI system and window is just a variable , becomes the container for everything (buttons, text, etc.)
window.title("Tic Tac Toe")  #this is the title of the window that appears above the window to actually know what it is 

current_player = "X"  
board = [""] * 9
buttons = []

# ---------------- WIN CHECK ----------------
def check_winner():
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    return None

# ---------------- BUTTON CLICK ----------------
def click(index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)

        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
            return

        if "" not in board:
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
            return

        # switch player
        current_player = "O" if current_player == "X" else "X"

# ---------------- RESET GAME ----------------
def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"

    for btn in buttons:
        btn.config(text="")

# ---------------- CREATE BUTTON GRID ----------------
for i in range(9):
    btn = tk.Button(
        window,
        text="",
        font=("Arial", 24),
        width=5,
        height=2,
        command=lambda i=i: click(i)
    )
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# ---------------- RUN APP ----------------
window.mainloop()