
from tkinter import *
from tkinter.font import BOLD
import math
import tkinter.messagebox

window = Tk()
window.geometry('495x545+0+0')
window.resizable(width=False, height=False)
window.title("Calculator")

calc = Frame(window)
calc.grid()

screen = Entry(calc, font=('calibre', 20), bg="green yellow", bd=10, width=31)
screen.grid(row=0, column=0, columnspan=6, ipady=40)

global value_1
global value_2
global op


def quit_program():
    quit = tkinter.messagebox.askyesno("Exit", "Do You Want To Exit?")
    if quit > 0:
        window.destroy()


def store_digit(number):
    global value_1
    value_1 = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(value_1)+str(number))


def point():
    global value_1
    value_1 = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(value_1)+str("."))


def ac():
    global ans
    ans = screen.get()
    screen.delete(0, END)


def ans():
    screen.delete(0, END)
    screen.insert(0, "ANS = "+str(ans))


def deel():
    global ans
    ans = screen.get()
    current = screen.get()[:-1]
    screen.delete(0, END)
    screen.insert(0, current)


def addition():
    global op
    global int_value_1
    op = "add"
    value_1 = screen.get()
    int_value_1 = float(value_1)
    screen.delete(0, END)


def sub():
    global op
    global int_value_1
    op = "sub"
    value_1 = screen.get()
    int_value_1 = float(value_1)
    screen.delete(0, END)


def div():
    global op
    global int_value_1
    op = "div"
    value_1 = screen.get()
    int_value_1 = float(value_1)
    screen.delete(0, END)


def mul():
    global op
    global int_value_1
    op = "mul"
    value_1 = screen.get()
    int_value_1 = float(value_1)
    screen.delete(0, END)


def equal():

    value_2 = float(screen.get())
    int_value_2 = float(value_2)
    if (op == "add"):
        store = int_value_1+int_value_2
        screen.delete(0, END)
        screen.insert(0, str(store))
    elif(op == "sub"):
        store = int_value_1-int_value_2
        screen.delete(0, END)
        screen.insert(0, str(store))
    elif(op == "mul"):
        store = int_value_1*int_value_2
        screen.delete(0, END)
        screen.insert(0, str(store))
    elif(op == "div"):
        store = int_value_1/int_value_2
        screen.delete(0, END)
        screen.insert(0, str(store))


# making buttons
# -------------------Row - 1 ----------------------------------------------------------------------------
btn_shift = Button(calc, text="SHIFT", bg="floral white", activebackground="SlateBlue1",
                   bd=2, width=10, height=2, relief=GROOVE).grid(row=1, column=0)
btn_alpha = Button(calc, text="ALPHA", bg="floral white", activebackground="SlateBlue1",
                   bd=2, width=10, height=2, relief=GROOVE).grid(row=1, column=1)
btn_mode = Button(calc, text="MODE", bg="floral white", activebackground="SlateBlue1",
                  bd=2, width=10, height=2, relief=GROOVE).grid(row=1, column=2)
btn_up = Button(calc, text="^", bg="SkyBlue2", activebackground="peach puff2",
                bd=2, width=10, height=2, relief=GROOVE).grid(row=1, column=3)
btn_setup = Button(calc, text="SETUP", bg="floral white", activebackground="SlateBlue1",
                   bd=2, width=10, height=2, relief=GROOVE).grid(row=1, column=4)
btn_on = Button(calc, text="ON", bg="floral white", activebackground="SlateBlue1",
                bd=2, width=10, height=2, relief=GROOVE).grid(row=1, column=5)

# -------------------Row - 2 ----------------------------------------------------------------------------
btn_left = Button(calc, text="<", bg="SkyBlue2", activebackground="peach puff2",
                  bd=2, width=10, height=2, relief=GROOVE).grid(row=2, column=2)
btn_replay = Button(calc, text="Replay", bg="floral white", activebackground="peach puff2",
                    bd=2, width=10, height=2, relief=GROOVE).grid(row=2, column=3)
btn_right = Button(calc, text=">", bg="SkyBlue2", activebackground="peach puff2",
                   bd=2, width=10, height=2, relief=GROOVE).grid(row=2, column=4)

# -------------------Row - 3 ----------------------------------------------------------------------------
btn_calc = Button(calc, text="CALC", bg="black", activebackground="SlateBlue1", bd=2,
                  width=10, height=2, relief=GROOVE, fg="floral white", command=equal).grid(row=3, column=0)
btn_integration = Button(calc, text="∫", bg="black", activebackground="SlateBlue1",
                         bd=2, width=10, height=2, relief=GROOVE, fg="floral white").grid(row=3, column=1)
btn_derivation = Button(calc, text="Dx y", bg="black", activebackground="SlateBlue1",
                        bd=2, width=10, height=2, relief=GROOVE, fg="floral white").grid(row=3, column=2)
btn_down = Button(calc, text="v", bg="SkyBlue2", activebackground="peach puff2",
                  bd=2, width=10, height=2, relief=GROOVE).grid(row=3, column=3)
btn_xpow_1 = Button(calc, text="X^-1", bg="black", activebackground="SlateBlue1",
                    bd=2, width=10, height=2, relief=GROOVE, fg="floral white").grid(row=3, column=4)
btn_loga = Button(calc, text="loga", bg="black", activebackground="SlateBlue1",
                  bd=2, width=10, height=2, relief=GROOVE, fg="floral white").grid(row=3, column=5)

# -------------------Row - 4 ----------------------------------------------------------------------------
btn_fraction = Button(calc, text="--", bg="black", activebackground="SlateBlue1",
                      bd=2, width=10, height=2, relief=GROOVE, fg="floral white").grid(row=4, column=0)
btn_sqroot = Button(calc, text="√", bg="black", activebackground="SlateBlue1",
                    bd=2, width=10, height=2, relief=GROOVE, fg="floral white").grid(row=4, column=1)
btn_xpow_2 = Button(calc, text="x^2", bg="black", activebackground="SlateBlue1",
                    bd=2, width=10, height=2, relief=GROOVE, fg="floral white").grid(row=4, column=2)
btn_xpow = Button(calc, text="x^", bg="black", activebackground="SlateBlue1", bd=2,
                  width=10, height=2, relief=GROOVE, fg="floral white").grid(row=4, column=3)
btn_log = Button(calc, text="log", bg="black", activebackground="SlateBlue1", bd=2,
                 width=10, height=2, relief=GROOVE, fg="floral white").grid(row=4, column=4)
btn_ln = Button(calc, text="ln", bg="black", activebackground="SlateBlue1", bd=2,
                width=10, height=2, relief=GROOVE, fg="floral white").grid(row=4, column=5)

# -------------------Row - 5 ----------------------------------------------------------------------------
btn_dash = Button(calc, text="(-)", bg="black", activebackground="SlateBlue1",
                  bd=2, width=10, height=2, relief=GROOVE, fg="floral white").grid(row=5, column=0)
btn_degree = Button(calc, text="°", bg="black", activebackground="SlateBlue1",
                    bd=2, width=10, height=2, relief=GROOVE, fg="floral white").grid(row=5, column=1)
btn_hyp = Button(calc, text="hyp", bg="black", activebackground="SlateBlue1", bd=2,
                 width=10, height=2, relief=GROOVE, fg="floral white").grid(row=5, column=2)
btn_sin = Button(calc, text="sin", bg="black", activebackground="SlateBlue1", bd=2,
                 width=10, height=2, relief=GROOVE, fg="floral white").grid(row=5, column=3)
btn_cos = Button(calc, text="cos", bg="black", activebackground="SlateBlue1", bd=2,
                 width=10, height=2, relief=GROOVE, fg="floral white").grid(row=5, column=4)
btn_tan = Button(calc, text="tan", bg="black", activebackground="SlateBlue1", bd=2,
                 width=10, height=2, relief=GROOVE, fg="floral white").grid(row=5, column=5)

# -------------------Row - 6 ----------------------------------------------------------------------------
btn_rcl = Button(calc, text="RCL", bg="black", activebackground="SlateBlue1", bd=2,
                 width=10, height=2, relief=GROOVE, fg="floral white").grid(row=6, column=0)
btn_eng = Button(calc, text="ENG", bg="black", activebackground="SlateBlue1", bd=2,
                 width=10, height=2, relief=GROOVE, fg="floral white").grid(row=6, column=1)
btn_bracket1 = Button(calc, text="(", bg="black", activebackground="SlateBlue1",
                      bd=2, width=10, height=2, relief=GROOVE, fg="floral white").grid(row=6, column=2)
btn_bracket2 = Button(calc, text=")", bg="black", activebackground="SlateBlue1",
                      bd=2, width=10, height=2, relief=GROOVE, fg="floral white").grid(row=6, column=3)
btn_sd = Button(calc, text="S<>D", bg="black", activebackground="SlateBlue1", bd=2,
                width=10, height=2, relief=GROOVE, fg="floral white").grid(row=6, column=4)
btn_mplus = Button(calc, text="M+", bg="black", activebackground="SlateBlue1",
                   bd=2, width=10, height=2, relief=GROOVE, fg="floral white").grid(row=6, column=5)

# -------------------Row - 7 ----------------------------------------------------------------------------
btn_seven = Button(calc, text="7", bg="floral white", activebackground="SlateBlue1", bd=2,
                   width=10, height=2, relief=GROOVE, command=lambda: store_digit(7)).grid(row=7, column=0)
btn_eight = Button(calc, text="8", bg="floral white", activebackground="SlateBlue1", bd=2,
                   width=10, height=2, relief=GROOVE, command=lambda: store_digit(8)).grid(row=7, column=1)
btn_nine = Button(calc, text="9", bg="floral white", activebackground="SlateBlue1", bd=2,
                  width=10, height=2, relief=GROOVE, command=lambda: store_digit(9)).grid(row=7, column=2)
btn_del = Button(calc, text="DEL", bg="orange red", activebackground="gold",
                 bd=2, width=10, height=2, relief=GROOVE, command=deel).grid(row=7, column=3)
btn_ac = Button(calc, text="AC", bg="orange red", activebackground="gold",
                bd=2, width=10, height=2, relief=GROOVE, command=ac).grid(row=7, column=4)

# -------------------Row - 8 ----------------------------------------------------------------------------
btn_four = Button(calc, text="4", bg="floral white", activebackground="SlateBlue1", bd=2,
                  width=10, height=2, relief=GROOVE, command=lambda: store_digit(4)).grid(row=8, column=0)
btn_five = Button(calc, text="5", bg="floral white", activebackground="SlateBlue1", bd=2,
                  width=10, height=2, relief=GROOVE, command=lambda: store_digit(5)).grid(row=8, column=1)
btn_six = Button(calc, text="6", bg="floral white", activebackground="SlateBlue1", bd=2,
                 width=10, height=2, relief=GROOVE, command=lambda: store_digit(6)).grid(row=8, column=2)
btn_mul = Button(calc, text="X", bg="floral white", activebackground="SlateBlue1",
                 bd=2, width=10, height=2, relief=GROOVE, command=mul).grid(row=8, column=3)
btn_div = Button(calc, text="/", bg="floral white", activebackground="SlateBlue1",
                 bd=2, width=10, height=2, relief=GROOVE, command=div).grid(row=8, column=4)

# -------------------Row - 7 ----------------------------------------------------------------------------
btn_one = Button(calc, text="1", bg="floral white", activebackground="SlateBlue1", bd=2,
                 width=10, height=2, relief=GROOVE, command=lambda: store_digit(1)).grid(row=9, column=0)
btn_two = Button(calc, text="2", bg="floral white", activebackground="SlateBlue1", bd=2,
                 width=10, height=2, relief=GROOVE, command=lambda: store_digit(2)).grid(row=9, column=1)
btn_three = Button(calc, text="3", bg="floral white", activebackground="SlateBlue1", bd=2,
                   width=10, height=2, relief=GROOVE, command=lambda: store_digit(3)).grid(row=9, column=2)
btn_plus = Button(calc, text="+", bg="floral white", activebackground="SlateBlue1",
                  bd=2, width=10, height=2, relief=GROOVE, command=addition).grid(row=9, column=3)
btn_sub = Button(calc, text="-", bg="floral white", activebackground="SlateBlue1",
                 bd=2, width=10, height=2, relief=GROOVE, command=sub).grid(row=9, column=4)

# -------------------Row - 8 ----------------------------------------------------------------------------
btn_zero = Button(calc, text="0", bg="floral white", activebackground="SlateBlue1", bd=2,
                  width=10, height=2, relief=GROOVE, command=lambda: store_digit(0)).grid(row=10, column=0)
btn_point = Button(calc, text=".", bg="floral white", activebackground="SlateBlue1",
                   bd=2, width=10, height=2, relief=GROOVE, command=point).grid(row=10, column=1)
btn_xpow_10 = Button(calc, text="x10^x", bg="floral white", activebackground="SlateBlue1",
                     bd=2, width=10, height=2, relief=GROOVE).grid(row=10, column=2)
btn_ans = Button(calc, text="Ans", bg="floral white", activebackground="SlateBlue1",
                 bd=2, width=10, height=2, relief=GROOVE, command=ans).grid(row=10, column=3)
btn_equal = Button(calc, text="=", bg="floral white", activebackground="SlateBlue1",
                   bd=2, width=10, height=2, relief=GROOVE, command=equal).grid(row=10, column=4)

# making a menu bar
menubar = Menu(calc)

exitmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Exit", menu=exitmenu)
exitmenu.add_command(label="Quit", command=quit_program)

window.config(menu=menubar)

window.mainloop()
