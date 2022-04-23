# ======== Copyright (c) 2021, FIT VUT Brno, All rights reserved. ============//
#
# Purpose:     GUI for calculator
#
# $Author:     FREDERIKA KMETOVA <xxkmeto00@stud.fit.vutbr.cz>
# $Date:       $2022-04-28
# ============================================================================//
#
# @file calc_GUI.py
# @author FREDERIKA KMETOVA
#
# @brief Implementation of GUI for calculator.

import tkinter as tk
import mathLibrary

# font sizes
NUMBERS_FONT = ("Courier New", 35)
EQUATIONS_FONT = ("Courier New", 20)
NUMBERS_COLOR = "black"
DISPLAY_COLOR = "#ddc0b4"
KEYBOARD_COLOR = "#d1ae9b"
BUTTONS_COLOR = "black"
OPERATORS_COLOR = "#c09175"


# class calculator
class Calculator:
    def __init__(self):
        self.calculator = tk.Tk()
        self.calculator.geometry("800x500")
        self.calculator.title("Calculator: by neFIT Team")
        self.calculator.configure(bg=DISPLAY_COLOR)
        self.display = self.make_display()
        self.every_expression = ""
        self.current_expression = ""
        self.numbers = {
            7: (1, 3), 8: (1, 4), 9: (1, 5),
            4: (2, 3), 5: (2, 4), 6: (2, 5),
            1: (3, 3), 2: (3, 4), 3: (3, 5),
            0: (4, 4),
        }
        self.operators = {
            '(': (1, 1), ')': (1, 2),  'DEL': (1, 6), 'C': (1, 7),
            '\u207f√': (2, 1), "\u00b2√": (2, 2), '/': (2, 6), '+': (2, 7),
            'x\u207f': (3, 1), 'x²': (3, 2), '*': (3, 6), '-': (3, 7),
            'SIN': (4, 1), 'COS': (4, 2), 'TAN': (4, 3), '.': (4, 5), '!': (4, 6), '=': (4, 7),
        }
        self.buttons_part = self.make_buttons_part()
        self.make_buttons_display()
        self.buttons_part.rowconfigure(0, weight=0)
        for x in range(1, 8):
            self.buttons_part.rowconfigure(x, weight=1)
            self.buttons_part.columnconfigure(x, weight=1)

    def run(self):
        self.calculator.mainloop()

    def make_display(self):
        display = tk.Frame(self.calculator, bg=DISPLAY_COLOR)
        display.pack(expand=True, fill="both")
        return display

    def make_buttons_part(self):
        button = tk.Button(self.calculator, bg=KEYBOARD_COLOR)
        button.pack(expand=True, fill="both")
        return button

    def make_buttons_display(self):
        for numbers, grid_value in self.numbers.items():
            button = tk.Button(self.buttons_part, text=str(numbers), bg="#aa6f5d", fg=BUTTONS_COLOR,
                               font=NUMBERS_FONT, borderwidth=0,)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
        for operators, grid_value in self.operators.items():
            button = tk.Button(self.buttons_part, text=str(operators), bg="#aa6f5d", fg=OPERATORS_COLOR,
                               font=NUMBERS_FONT, borderwidth=0,)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)


# running calculator
if __name__ == "__main__":
    calc = Calculator()
    calc.run()

# ------ End of file calc_GUI.py ------
