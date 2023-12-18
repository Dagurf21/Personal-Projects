import tkinter as tk
from tkinter import messagebox

# 2. Create the board
def create_board():
    for x in range(3):
        for y in range(3):
            #Create buttons
            button = tk.Button(window,
                               text="", 
                               font=("Arial", 50),
                               height=2,
                               width=6,
                               bg="ligthblue",
                               command=lambda row=x, col=y: handle_click(row, col))
            button.grid(row=x, 
                        column=y, 
                        sticky="nsew")



def main():
    # 1. Create Window
    window = tk.Tk()
    window.title("Tic Tac Toe")
    
    create_board()

if __name__ == "__main__":
    main()