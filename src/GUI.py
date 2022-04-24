from tkinter import *
import mathLibrary as math


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