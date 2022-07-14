from tkinter import *
from tkinter import messagebox


t = Tk()
t.title('Tic Tac Toe')

# X Starts
clicked = True
count = 0


def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

# Check to see if there is a winner
def if_winner():
    global winner
    winner = False
    # Check for X
    if b1['text'] == "X" and b2['text'] == 'X' and b3['text'] == 'X':
        b1.config(highlightbackground="green")
        b2.config(highlightbackground="green")
        b3.config(highlightbackground="green")

        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_all_buttons()

    elif b4['text'] == "X" and b5['text'] == 'X' and b6['text'] == 'X':
        b4.config(highlightbackground="green")
        b5.config(highlightbackground="green")
        b6.config(highlightbackground="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_all_buttons()

    elif b7['text'] == "X" and b8['text'] == 'X' and b9['text'] == 'X':
        b7.config(highlightbackground="green")
        b8.config(highlightbackground="green")
        b9.config(highlightbackground="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_all_buttons()

    elif b1['text'] == "X" and b4['text'] == 'X' and b7['text'] == 'X':
        b1.config(highlightbackground="green")
        b4.config(highlightbackground="green")
        b7.config(highlightbackground="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_all_buttons()

    elif b2['text'] == "X" and b5['text'] == 'X' and b8['text'] == 'X':
        b2.config(highlightbackground="green")
        b5.config(highlightbackground="green")
        b8.config(highlightbackground="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_all_buttons()

    elif b3['text'] == "X" and b6['text'] == 'X' and b9['text'] == 'X':
        b3.config(highlightbackground="green")
        b6.config(highlightbackground="green")
        b9.config(highlightbackground="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_all_buttons()

    elif b1['text'] == "X" and b5['text'] == 'X' and b9['text'] == 'X':
        b1.config(highlightbackground="green")
        b5.config(highlightbackground="green")
        b9.config(highlightbackground="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_all_buttons()

    elif b3['text'] == "X" and b5['text'] == 'X' and b7['text'] == 'X':
        b3.config(highlightbackground="green")
        b5.config(highlightbackground="green")
        b7.config(highlightbackground="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_all_buttons()


    #Check for O
    elif b1['text'] == "O" and b2['text'] == 'O' and b3['text'] == 'O':
        b1.config(highlightbackground="green")
        b2.config(highlightbackground="green")
        b3.config(highlightbackground="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_all_buttons()

    elif b4['text'] == "O" and b5['text'] == 'O' and b6['text'] == 'O':
        b4.config(highlightbackground="green")
        b5.config(highlightbackground="green")
        b6.config(highlightbackground="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_all_buttons()

    elif b7['text'] == "O" and b8['text'] == 'O' and b9['text'] == 'O':
        b7.config(highlightbackground="green")
        b8.config(highlightbackground="green")
        b9.config(highlightbackground="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_all_buttons()

    elif b1['text'] == "O" and b4['text'] == 'O' and b7['text'] == 'O':
        b1.config(highlightbackground="green")
        b4.config(highlightbackground="green")
        b7.config(highlightbackground="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_all_buttons()

    elif b2['text'] == "O" and b5['text'] == 'O' and b8['text'] == 'O':
        b2.config(highlightbackground="green")
        b5.config(highlightbackground="green")
        b8.config(highlightbackground="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_all_buttons()

    elif b3['text'] == "O" and b6['text'] == 'O' and b9['text'] == 'O':
        b3.config(highlightbackground="green")
        b6.config(highlightbackground="green")
        b9.config(highlightbackground="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_all_buttons()

    elif b1['text'] == "O" and b5['text'] == 'O' and b9['text'] == 'O':
        b1.config(highlightbackground="green")
        b5.config(highlightbackground="green")
        b9.config(highlightbackground="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_all_buttons()

    elif b3['text'] == "O" and b5['text'] == 'O' and b7['text'] == 'O':
        b3.config(highlightbackground="green")
        b5.config(highlightbackground="green")
        b7.config(highlightbackground="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_all_buttons()

#Check for tie
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        disable_all_buttons()


def changeVal(b):
    global clicked, count

    if b['text'] == '' and clicked == True:
        b['text'] = 'X'
        clicked = False
        count += 1
        if_winner()
    elif b['text'] == '' and clicked == False:
        b['text'] = 'O'
        clicked = True
        count += 1
        if_winner()
    else:
        messagebox.showerror("Tic Tac Toe", "Please select a blank box")


def play_again():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0
    # Grid buttons
    b1 = Button(t, text="", height=4, width=8, bg="white", highlightbackground='black', font="Times 15 bold", command=lambda: changeVal(b1))
    b2 = Button(t, text="", height=4, width=8, bg="white", highlightbackground='black', font="Times 15 bold", command=lambda: changeVal(b2))
    b3 = Button(t, text="", height=4, width=8, bg="white", highlightbackground='black', font="Times 15 bold", command=lambda: changeVal(b3))


    b4 = Button(t, text="", height=4, width=8, bg="white", highlightbackground='black', font="Times 15 bold", command=lambda: changeVal(b4))
    b5 = Button(t, text="", height=4, width=8, bg="white", highlightbackground='black', font="Times 15 bold", command=lambda: changeVal(b5))
    b6 = Button(t, text="", height=4, width=8, bg="white", highlightbackground='black', font="Times 15 bold", command=lambda: changeVal(b6))


    b7 = Button(t, text="", height=4, width=8, bg="white", highlightbackground='black', font="Times 15 bold", command=lambda: changeVal(b7))
    b8 = Button(t, text="", height=4, width=8, bg="white", highlightbackground='black', font="Times 15 bold", command=lambda: changeVal(b8))
    b9 = Button(t, text="", height=4, width=8, bg="white", highlightbackground='black', font="Times 15 bold", command=lambda: changeVal(b9))

    # Button grid assign

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


game_menu = Menu(t)
t.config(menu=game_menu)

options_menu = Menu(game_menu, tearoff=False)
game_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Restart", command=play_again)

play_again()
t.mainloop()