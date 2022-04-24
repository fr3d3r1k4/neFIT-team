# ======== Copyright (c) 2021, FIT VUT Brno, All rights reserved. ============//
#
# Purpose:     GUI for calculator
#
# $Author:     FREDERIKA KMETOVA <xkmeto00@stud.fit.vutbr.cz>
# $Date:       $2022-04-28
# ============================================================================//
#
# @file calc_GUI.py
# @author FREDERIKA KMETOVA
#
# @brief Implementation of GUI for calculator.

from tkinter import *

DISPLAY_COLOR = "#ddc0b4"
KEYBOARD_COLOR = "#d1ae9b"
NUMBERS_COLOR = "black"
NUMBERS_FONT = ("Courier New", 30)
OPERATORS_FONT = ("Courier New", 20)
OPERATORS_COLOR = "#c09175"
DISPLAY_FRAME = "#aa6f5d"

calc = Tk()
calc.title("Calculator by neFit Team")
calc.geometry("560x550")
calc.resizable(0, 0)
calc.configure(bg=DISPLAY_COLOR)

display = LabelFrame(calc, bg=DISPLAY_FRAME)
display.grid(row=0, column=0, padx=20, pady=20, sticky=NSEW)
display_entry = Entry(display, bg=DISPLAY_COLOR, font=NUMBERS_FONT)
display_entry.grid(row=1, column=2, padx=40, pady=50)
keyboard = LabelFrame(calc, bg="white")
keyboard.grid(row=2, column=0, padx=10, pady=10)


def click(value):
    global operation
    text = StringVar()
    operation = operation + str(value)
    text.set(operation)


def delete_all():
    text = StringVar()
    text.set('')


# @TODO HELP WINDOW
def help():
    help_text = StringVar()
    help = Tk()
    help_button = Label(help, text="long help that i will do later")
    help_button.pack()


def radical():
    global number
    text = StringVar()
    number = number + " radical "
    text.set(number)


def n_square():
    global number
    text = StringVar()
    number = number + " n_square "
    text.set(number)


def square():
    global number
    text = StringVar()
    number = number + " square "
    text.set(number)


def equal():
    global operator
    text = StringVar()
    add = str(eval(operator))
    text.set(add)
    operator = ''


# (
button_bracket1 = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="(", command=lambda: click("("),
                         height=2, width=2)
button_bracket1.grid(row=1, column=1, padx=1, pady=1)
# )
button_bracket2 = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text=")", command=lambda: click(")"),
                         height=2, width=2)
button_bracket2.grid(row=1, column=2, padx=1, pady=1)
# 7
button_seven = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="7", command=lambda: click(7),
                      height=2, width=2)
button_seven.grid(row=1, column=3, padx=1, pady=1)
# 8
button_eight = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="8", command=lambda: click(8),
                      height=2, width=2)
button_eight.grid(row=1, column=4, padx=1, pady=1)
# 9
button_nine = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="9", command=lambda: click(9),
                     height=2, width=2)
button_nine.grid(row=1, column=5, padx=1, pady=1)
# help
button_help = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="?", command=help,
                     height=2, width=2)
button_help.grid(row=1, column=6, padx=1, pady=1)
# c
button_c = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="C", command=delete_all,
                  height=2, width=2)
button_c.grid(row=1, column=7, padx=1, pady=1)

# n radical
button_n_radical = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="\u207f√", command=radical,
                          height=2, width=2)
button_n_radical.grid(row=2, column=1, padx=1, pady=1)
# radical
button_2_radical = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="\u00b2√", command=radical,
                          height=2, width=2)
button_2_radical.grid(row=2, column=2, padx=1, pady=1)
# 4
button_four = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="4", command=lambda: click(4),
                     height=2, width=2)
button_four.grid(row=2, column=3, padx=1, pady=1)
# 5
button_five = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="5", command=lambda: click(5),
                     height=2, width=2)
button_five.grid(row=2, column=4, padx=1, pady=1)
# 6
button_six = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="6", command=lambda: click(6),
                    height=2, width=2)
button_six.grid(row=2, column=5, padx=1, pady=1)
# /
button_divide = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="/", command=lambda: click("/"),
                       height=2, width=2)
button_divide.grid(row=2, column=6, padx=1, pady=1)
# +
button_plus = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="+", command=lambda: click("+"),
                     height=2, width=2)
button_plus.grid(row=2, column=7, padx=1, pady=1)

# x^n
button_n_square = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="x\u207f", command=n_square,
                         height=2, width=2)
button_n_square.grid(row=3, column=1, padx=1, pady=1)
# x^2
button_2_square = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="x²", command=square,
                         height=2, width=2)
button_2_square.grid(row=3, column=2, padx=1, pady=1)
# 1
button_one = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="1", command=lambda: click(1),
                    height=2, width=2)
button_one.grid(row=3, column=3, padx=1, pady=1)
# 2
button_two = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="2", command=lambda: click(2),
                    height=2, width=2)
button_two.grid(row=3, column=4, padx=1, pady=1)
# 3
button_three = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="3", command=lambda: click(3),
                      height=2, width=2)
button_three.grid(row=3, column=5, padx=1, pady=1)
# *
button_2_square = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="*", command=lambda: click("*"),
                         height=2, width=2)
button_2_square.grid(row=3, column=6, padx=1, pady=1)
# -
button_2_square = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="-", command=lambda: click("-"),
                         height=2, width=2)
button_2_square.grid(row=3, column=7, padx=1, pady=1)

# sin
button_sin = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="sin", command=lambda: click("sin"),
                    height=2, width=2)
button_sin.grid(row=4, column=1, padx=1, pady=1)
# cos
button_cos = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="cos", command=lambda: click("cos"),
                    height=2, width=2)
button_cos.grid(row=4, column=2, padx=1, pady=1)
# tan
button_tan = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="tan", command=lambda: click("tan"),
                    height=2, width=2)
button_tan.grid(row=4, column=3, padx=1, pady=1)
# 0
button_zero = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="0", command=lambda: click(0),
                     height=2, width=2)
button_zero.grid(row=4, column=4, padx=1, pady=1)
# .
button_dot = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text=".", command=lambda: click("."),
                    height=2, width=2)
button_dot.grid(row=4, column=5, padx=1, pady=1)
# !
button_factorial = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="!", command=lambda: click("!"),
                          height=2, width=2)
button_factorial.grid(row=4, column=6, padx=1, pady=1)
# =
button_equals = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="=", command=equal,
                       height=2, width=2)
button_equals.grid(row=4, column=7, padx=1, pady=1)

calc.mainloop()

