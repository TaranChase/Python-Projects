# Title: Tic Tac Toe game with GUI using tkinter in Python
#  Author: jainj2305
#  Date: 08 Jan, 2021
#  Code version: Python3
#  Availability: https://www.geeksforgeeks.org
# ----------------------------------------------
# (Version Python3)[Source code].https://www.geeksforgeeks.org
#--------------------------------------------------------------

#Import libraries
import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

# Variable used to decide turn of Player
sign = 0

# Empty board
global board
board = [[" " for x in range(3)] for y in range(3)]

# Checks winner
def check_winner(b, c):
    return ((b[0][0] == c and b[0][1] == c and b[0][2] == c) or
            (b[1][0] == c and b[1][1] == c and b[1][2] == c) or
            (b[2][0] == c and b[2][1] == c and b[2][2] == c) or
            (b[0][0] == c and b[1][0] == c and b[2][0] == c) or
            (b[0][1] == c and b[1][1] == c and b[2][1] == c) or
            (b[0][2] == c and b[1][2] == c and b[2][2] == c) or
            (b[0][0] == c and b[1][1] == c and b[2][2] == c) or
            (b[0][2] == c and b[1][1] == c and b[2][0] == c))

# Text to display on button when playing with another play
def display_text_wp(i, j, g_b, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign = sign + 1
        button[i][j].config(text=board[i][j])
    if check_winner(board, "X"):
        g_b.destroy()
        msg = messagebox.showinfo("Congratulations!", "Player 1 wins")
    elif check_winner(board, "O"):
        g_b.destroy()
        msg = messagebox.showinfo("Congratulations!", "Player 2 wins")
    elif(full_b()):
        g_b.destroy()
        msg = messagebox.showinfo("Draw", "Draw!")

# Checks if player can push button
def btn_push(i, j):
    return board[i][j] == " "

# Check if board is full
def full_b():
    flag =True
    for i in board:
        if(i.count(' ')> 0):
            flag = False
    return flag

# Multiplayer GUI
def gameboard_pl(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        r = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(display_text_wp, i, j, game_board, l1, l2)
            button[i][j] = Button(game_board, bd=6, command=get_t, height=6, width=12)
            button[i][j].grid(row=r, column=n)
    game_board.mainloop()

# Decides systems next move
def P_C():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for l in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = l
                if check_winner(boardcopy, l):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner)-1)
            return corner[move]

        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge)-1)
            return edge[move]

# Text Display on button when playing with system
def display_text_ws(i, j, g_b, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign = sign + 1
        button[i][j].config(text=board[i][j])
    x = True
    if check_winner(board, "X"):
        g_b.destroy()
        x = False
        msg = messagebox.showinfo("Winner", "Player wins")
    elif check_winner(board, "O"):
        g_b.destroy()
        x = False
        msg = messagebox.showinfo("Winner", "Computer wins.")
    elif(full_b()):
        g_b.destroy()
        x = False
        msg = messagebox.showinfo("Draw", "Draw!")
    if(x):
        if sign % 2 != 0:
            move = P_C()
            button[move[0]][move[1]].config(state=DISABLED)
            display_text_wp(move[0], move[1], g_b, l1, l2)

# Single Player GUI
def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        r = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(display_text_ws, i, j, game_board, l1, l2)
            button[i][j] = Button(game_board, bd=6, command=get_t, height=6, width=12)
            button[i][j].grid(row=r, column=n)
    game_board.mainloop()

# Initialize game board to play with system
def w_s(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text = "Player : X", width = 12)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text = "Computer: 0", width=12, state=DISABLED)
    l2.grid(row = 2, column = 1)
    gameboard_pc(game_board, l1, l2)


# Initialize game board to play with another Player
def w_p(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text = "Player 1 : X", width = 12)

    l1.grid(row = 1, column = 1)
    l2 = Button(game_board, text = "Player 2 : O", width=12, state=DISABLED)
    l2.grid(row=2, column=1)
    gameboard_pl(game_board, l1, l2)


#Main Function
def play():
    t = Tk()
    t.geometry("230x230")
    t.title("Tic Tac Toe")
    w_pc = partial(w_s, t)
    w_pl = partial(w_p, t)

    title = Label(t, text="Let's Play!", activeforeground = "white", activebackground = "black", bg="white", fg="black", width=500, font="arial", bd=10)

    b1 = Button(t, text="Single Player", command = w_pc, activeforeground = "#ADADAD", activebackground = "#D2D0D0", bg="#ADADAD", fg="black", width=500, font="arial", bd=6)

    b2 = Button(t, text="Multi Player", command = w_pl, activeforeground = "#ADADAD", activebackground = "#D2D0D0", bg="#ADADAD", fg="black", width=500, font="arial", bd=6)

    b3 = Button(t, text="Exit", command =t.quit, activeforeground = "#ADADAD", activebackground = "#D2D0D0", bg="#ADADAD", fg="black", width=500, font="arial", bd=6)

    title.pack(side = 'top')
    b1.pack(side = 'top')
    b2.pack(side = 'top')
    b3.pack(side = 'top')
    t.mainloop()

#Execute
if __name__ == '__main__':
    play()
