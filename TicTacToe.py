from tkinter import *
import tkinter.messagebox as t

tk = Tk()
tk.title("TicTacToe")


isCross = True;
turns = 0


def main():
    global btn1, btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9

    lbl = Label(tk, text="TicTacToe", font=("Arial Bold", 50)).grid(row=0, column=2)

    btn1 = Button(tk, text="", command=lambda: box(btn1), font=("Arial Bold", 30), bg="black", fg="white", width=6,
                  height=5)
    btn1.grid(row=2, column=1, sticky="nsew")

    btn2 = Button(tk, text="", command=lambda: box(btn2), font=("Arial Bold", 30), bg="black", fg="white", width=6,
                  height=5)
    btn2.grid(row=2, column=2, sticky="nsew")

    btn3 = Button(tk, text="", command=lambda: box(btn3), font=("Arial Bold", 30), bg="black", fg="white", width=6,
                  height=5)
    btn3.grid(row=2, column=3, sticky="nsew")

    btn4 = Button(tk, text="", command=lambda: box(btn4), font=("Arial Bold", 30), bg="black", fg="white", width=6,
                  height=5)
    btn4.grid(row=3, column=1, sticky="nsew")

    btn5 = Button(tk, text="", command=lambda: box(btn5), font=("Arial Bold", 30), bg="black", fg="white", width=6,
                  height=5)
    btn5.grid(row=3, column=2, sticky="nsew")

    btn6 = Button(tk, text="", command=lambda: box(btn6), font=("Arial Bold", 30), bg="black", fg="white", width=6,
                  height=5)
    btn6.grid(row=3, column=3, sticky="nsew")

    btn7 = Button(tk, text="", command=lambda: box(btn7), font=("Arial Bold", 30), bg="black", fg="white", width=6,
                  height=5)
    btn7.grid(row=4, column=1, sticky="nsew")

    btn8 = Button(tk, text="", command=lambda: box(btn8), font=("Arial Bold", 30), bg="black", fg="white", width=6,
                  height=5)
    btn8.grid(row=4, column=2, sticky="nsew")

    btn9 = Button(tk, text="", command=lambda: box(btn9), font=("Arial Bold", 30), bg="black", fg="white", width=6,
                  height=5)
    btn9.grid(row=4, column=3, sticky="nsew")

    menubar = Menu(tk)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New Game", command=reset)
    filemenu.add_command(label="Exit", command=tk.quit)
    menubar.add_cascade(label="Game", menu=filemenu)

    tk.config(menu=menubar)

    tk.mainloop()


def highlightWinningCombo(button1, button2, button3):
    button1.config(bg="green")
    button2.config(bg="green")
    button3.config(bg="green")


def disableAll():
    for i in range(1,10):
        eval('btn' + str(i)).config(state='disabled')


def checkforwin():
    if (btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or
            btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X' or
            btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X' or
            btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X' or
            btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X' or
            btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or
            btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X' or
            btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X' or
            btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X'):

        if btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X':
            highlightWinningCombo(btn1, btn2, btn3)

        if btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X':
            highlightWinningCombo(btn4, btn5, btn6)
        if btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X':
            highlightWinningCombo(btn7, btn8, btn9)
        if btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X':
            highlightWinningCombo(btn1, btn5, btn9)
        if btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X':
            highlightWinningCombo(btn3, btn5, btn7)
        if btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X':
            highlightWinningCombo(btn1, btn4, btn7)
        if btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X':
            highlightWinningCombo(btn2, btn5, btn8)
        if btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X':
            highlightWinningCombo(btn3, btn6, btn9)
        t.showinfo("Player 1 wins!!", "Player 1 wins!!")
        disableAll()

    elif(btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
          btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O' or
          btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O' or
          btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O' or
          btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O' or
          btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
          btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O' or
          btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O' or
          btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O'):

        if btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O':
            highlightWinningCombo(btn1, btn2, btn3)

        if btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O':
            highlightWinningCombo(btn4, btn5, btn6)
        if btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O':
            highlightWinningCombo(btn7, btn8, btn9)
        if btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O':
            highlightWinningCombo(btn1, btn5, btn9)
        if btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O':
            highlightWinningCombo(btn3, btn5, btn7)
        if btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O':
            highlightWinningCombo(btn1, btn4, btn7)
        if btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O':
            highlightWinningCombo(btn2, btn5, btn8)
        if btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O':
            highlightWinningCombo(btn3, btn6, btn9)
            disableAll()

        t.showinfo("Player 2 wins!!","Player 2 wins!!")

    elif turns == 9:
        t.showinfo("It's a tie!!","It's a tie!!")

    else:
        return False


def box(btn):
    global isCross, turns
    if isCross:
        btn.config(text="X")
        btn.configure(state=DISABLED)
        isCross = False
        turns += 1

    else:
        btn.config(text="O")
        btn.configure(state=DISABLED)
        isCross = True
        turns += 1

    checkforwin()


def reset():
    global turns,isCross
    turns = 0
    isCross = True
    for i in range(1,10):
        eval('btn'+str(i)).config(text = "")
        eval('btn' + str(i)).config(state='normal')
        eval('btn' + str(i)).config(bg = "black")


if __name__ == '__main__':
    main()

