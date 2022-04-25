##  @file calc_GUI.py
#   @brief Implementation of GUI for calculator.
#   @author FREDERIKA KMETOVA
#   @date 2022-04-28

from tkinter import *
import GUI

# ========================== DEFINING COLORS AND FONTS ==========================
DISPLAY_COLOR = "#ddc0b4"
KEYBOARD_COLOR = "#d1ae9b"
NUMBERS_COLOR = "white"
NUMBERS_FONT = ("Courier New", 20)
OPERATORS_COLOR = "#c09175"
DISPLAY_FRAME = "#aa6f5d"

# ========================== MAKING OF CALCULATOR WINDOW =========================
calc = Tk()
calc.title("Calculator by neFit Team")
calc.geometry("450x430")
calc.configure(bg=DISPLAY_COLOR)
equation = StringVar()

# ======================== MAKING OF DISPLAY AND KEYBOARD ========================
display = LabelFrame(calc, bg=DISPLAY_FRAME)
display.grid(row=0, column=0, padx=20, pady=20, sticky=NSEW)
display_entry = Entry(display, textvariable=equation, bg=DISPLAY_COLOR, font=NUMBERS_FONT)
display_entry.grid(row=1, column=2, padx=40, pady=50)
keyboard = LabelFrame(calc, bg="white")
keyboard.grid(row=2, column=0, padx=10, pady=10)


def equals():
    entry = display_entry.get()
    entry = GUI.solve(entry)
    if entry is False:
        entry = "Invalid input."
    display_entry.delete(0, END)
    display_entry.insert(0, str(entry))


def wrong_input():
    if display_entry.get() == "Invalid input.":
        display_entry.delete(0, END)

# ========================== FIRST ROW ===========================


def seven():
    wrong_input()
    display_entry.insert(END, "7")


def eight():
    wrong_input()
    display_entry.insert(END, "8")


def nine():
    wrong_input()
    display_entry.insert(END, "9")


def bracket1():
    wrong_input()
    display_entry.insert(END, "(")


def bracket2():
    wrong_input()
    display_entry.insert(END, ")")


def delete():
    wrong_input()
    display_entry.delete(len(display_entry.get()) - 1, END)


def delete_all():
    wrong_input()
    display_entry.delete(0, END)


# (
button_bracket1 = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="(", command=bracket1, height=1, width=3)
button_bracket1.grid(row=1, column=1, padx=1, pady=1)
# )
button_bracket2 = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text=")", command=bracket2, height=1, width=3)
button_bracket2.grid(row=1, column=2, padx=1, pady=1)
# 7
button_seven = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="7", command=seven,height=1, width=3)
button_seven.grid(row=1, column=3, padx=1, pady=1)
# 8
button_eight = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="8", command=eight,height=1, width=3)
button_eight.grid(row=1, column=4, padx=1, pady=1)
# 9
button_nine = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="9", command=nine, height=1, width=3)
button_nine.grid(row=1, column=5, padx=1, pady=1)
# DEL
button_del = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="DEL", command=delete, height=1, width=3)
button_del.grid(row=1, column=6, padx=1, pady=1)
# c
button_c = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="C", command=delete_all, height=1, width=3)
button_c.grid(row=1, column=7, padx=1, pady=1)


# ========================== SECOND ROW ===========================


def n_radical():
    wrong_input()
    display_entry.insert(END, "\u207f√")


def radical():
    wrong_input()
    display_entry.insert(END, "\u221A")


def four():
    wrong_input()
    display_entry.insert(END, "4")


def five():
    wrong_input()
    display_entry.insert(END, "5")


def six():
    wrong_input()
    display_entry.insert(END, "6")


def divide():
    wrong_input()
    display_entry.insert(END, "/")


def plus():
    wrong_input()
    display_entry.insert(END, "+")


# n radical
button_n_radical = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="\u207f√", command=n_radical, height=1,
                          width=3)
button_n_radical.grid(row=2, column=1, padx=1, pady=1)
# radical
button_2_radical = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="\u221A", command=radical, height=1,
                          width=3)
button_2_radical.grid(row=2, column=2, padx=1, pady=1)
# 4
button_four = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="4", command=four, height=1, width=3)
button_four.grid(row=2, column=3, padx=1, pady=1)
# 5
button_five = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="5", command=five, height=1, width=3)
button_five.grid(row=2, column=4, padx=1, pady=1)
# 6
button_six = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="6", command=six, height=1, width=3)
button_six.grid(row=2, column=5, padx=1, pady=1)
# /
button_divide = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="/", command=divide, height=1, width=3)
button_divide.grid(row=2, column=6, padx=1, pady=1)
# +
button_plus = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="+", command=plus, height=1, width=3)
button_plus.grid(row=2, column=7, padx=1, pady=1)


# ========================== THIRD ROW ===========================


def n_square():
    wrong_input()
    display_entry.insert(END, "x\u207f")


def square():
    wrong_input()
    display_entry.insert(END, "x²")


def one():
    wrong_input()
    display_entry.insert(END, "1")


def two():
    wrong_input()
    display_entry.insert(END, "2")


def three():
    wrong_input()
    display_entry.insert(END, "3")


def multiply():
    wrong_input()
    display_entry.insert(END, "*")


def minus():
    wrong_input()
    display_entry.insert(END, "-")


# x^n
button_n_square = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="x\u207f", command=n_square, height=1,
                         width=3)
button_n_square.grid(row=3, column=1, padx=1, pady=1)
# x^2
button_2_square = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="x²", command=square, height=1, width=3)
button_2_square.grid(row=3, column=2, padx=1, pady=1)
# 1
button_one = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="1", command=one, height=1, width=3)
button_one.grid(row=3, column=3, padx=1, pady=1)
# 2
button_two = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="2", command=two, height=1, width=3)
button_two.grid(row=3, column=4, padx=1, pady=1)
# 3
button_three = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="3", command=three, height=1, width=3)
button_three.grid(row=3, column=5, padx=1, pady=1)
# *
button_multiply = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="*", command=multiply, height=1, width=3)
button_multiply.grid(row=3, column=6, padx=1, pady=1)
# -
button_minus = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="-", command=minus, height=1, width=3)
button_minus.grid(row=3, column=7, padx=1, pady=1)


# ========================== FOURTH ROW ===========================

def sin():
    wrong_input()
    display_entry.insert(END, "sin(")


def cos():
    wrong_input()
    display_entry.insert(END, "cos(")


def help_me():
    wrong_input()
    help_button = Tk()
    help_button.title("Help Window")
    help_window = Label(help_button, text="long help that i will do later")
    help_window.pack()


def zero():
    wrong_input()
    display_entry.insert(END, "0")


def dot():
    wrong_input()
    display_entry.insert(END, ".")


def factorial():
    wrong_input()
    display_entry.insert(END, "!")


# sin
button_sin = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="sin", command=sin, height=1, width=3)
button_sin.grid(row=4, column=1, padx=1, pady=1)
# cos
button_cos = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="cos", command=cos, height=1, width=3)
button_cos.grid(row=4, column=2, padx=1, pady=1)
# help
button_help = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="?", command=help_me, height=1, width=3)
button_help.grid(row=4, column=3, padx=1, pady=1)
# 0
button_zero = Button(keyboard, bg=NUMBERS_COLOR, font=NUMBERS_FONT, text="0", command=zero, height=1, width=3)
button_zero.grid(row=4, column=4, padx=1, pady=1)
# .
button_dot = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text=".", command=dot, height=1, width=3)
button_dot.grid(row=4, column=5, padx=1, pady=1)
# !
button_factorial = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="!", command=factorial, height=1,
                          width=3)
button_factorial.grid(row=4, column=6, padx=1, pady=1)
# =
button_equals = Button(keyboard, bg=OPERATORS_COLOR, font=NUMBERS_FONT, text="=", command=equals, height=1, width=3)
button_equals.grid(row=4, column=7, padx=1, pady=1)

# ========================== CALCULATOR RUNNING ===========================

calc.mainloop()

# ---- End of file calc_GUI.py ----
