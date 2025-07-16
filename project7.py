import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    combos = [[0,1,2],[3,4,5],[6,7,8],
              [0,3,6],[1,4,7],[2,5,8],
              [0,4,8],[2,4,6]]
    for combo in combos:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            for i in combo:
                buttons[i].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            root.after(1000, reset_game)  # Reset after 1 second
            return

    # If all buttons are filled and no winner
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw! Starting a new game.")
        root.after(1000, reset_game)

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

def reset_game():
    global current_player, winner
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")
    current_player = "X"
    winner = False
    label.config(text=f"Player {current_player}'s turn")

# UI setup
root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("normal", 25), width=6, height=2,
                    command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

current_player = "X"
winner = False

label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
