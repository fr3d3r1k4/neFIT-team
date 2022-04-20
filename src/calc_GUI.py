import tkinter as tk

# font sizes
NUMBERS_FONT = ("Courier New", 35)
EQUATIONS_FONT = ("Courier New", 20)


# class calculator
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x700")
        self.window.resizable(0, 0)
        self.window.title("Calculator: by neFIT Team")
        self.numbers = {
            '.': (4, 1), 0: (4, 2),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            7: (1, 1), 8: (1, 2), 9: (1, 3)
        }

    def run(self):
        self.window.mainloop()

        
#running calculator
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
