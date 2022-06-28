import tkinter as tk
from tkinter import ttk
from functools import partial

from processor import Processor

LARGEFONT = ("Verdana", 35)
SMALLFONT = ("Verdana", 18)

class CalculatorFrame(tk.Frame):

    def __init__(self, container):
        super().__init__(container)
        self.processor = Processor()
        self.grid(sticky = tk.N + tk.S + tk.E + tk.W)
        self.create_widgets()

    def create_widgets(self):
        for row in range(6):
            self.grid_rowconfigure(row, weight = 1)
        for column in range(4):
            self.grid_columnconfigure(column, weight = 1)

        # field options
        options = {'padx': 0,
                   'pady': 0,
                   'ipadx': 0,
                   'ipady': 0}

        # display
        self.display = tk.Label(self,
                                text = '0',
                                font = LARGEFONT,
                                fg = 'black',
                                borderwidth = 6)
        self.display.grid(column = 0,
                          row = 0,
                          columnspan = 4,
                          sticky = tk.E,
                          **options)

        # buttons
        buttons_settings = [
            {'text': 'AC', 'row': 1, 'column': 0, 'bg': 'darkgray'},
            {'text': '+/-', 'row': 1, 'column': 1, 'bg': 'darkgray'},
            {'text': '%', 'row': 1, 'column': 2, 'bg': 'darkgray'},
            {'text': '÷', 'row': 1, 'column': 3, 'bg': 'orange'},
            {'text': '7', 'row': 2, 'column': 0, 'bg': 'gray'},
            {'text': '8', 'row': 2, 'column': 1, 'bg': 'gray'},
            {'text': '9', 'row': 2, 'column': 2, 'bg': 'gray'},
            {'text': 'x', 'row': 2, 'column': 3, 'bg': 'orange'},
            {'text': '4', 'row': 3, 'column': 0, 'bg': 'gray'},
            {'text': '5', 'row': 3, 'column': 1, 'bg': 'gray'},
            {'text': '6', 'row': 3, 'column': 2, 'bg': 'gray'},
            {'text': '-', 'row': 3, 'column': 3, 'bg': 'orange'},
            {'text': '1', 'row': 4, 'column': 0, 'bg': 'gray'},
            {'text': '2', 'row': 4, 'column': 1, 'bg': 'gray'},
            {'text': '3', 'row': 4, 'column': 2, 'bg': 'gray'},
            {'text': '+', 'row': 4, 'column': 3, 'bg': 'orange'},
            {'text': '0', 'row': 5, 'column': 0, 'bg': 'gray', 'columnspan': 2},
            {'text': '.', 'row': 5, 'column': 2, 'bg': 'gray'},
            {'text': '=', 'row': 5, 'column': 3, 'bg': 'orange'},
        ]
        self.buttons = []
        for d in buttons_settings:
            button = tk.Button(self,
                               text = d['text'],
                               command = partial(self.keypressed, d['text']),
                               font = SMALLFONT,
                               bd = 0,
                               bg = 'systemTransparent',
                               # bg = d['bg'],
                               relief = 'flat',
                               activebackground = '#333',
                               highlightbackground = '#333',
                               default = 'normal')
            button.grid(column = d['column'],
                        row = d['row'],
                        sticky = tk.N + tk.E + tk.S + tk.W,
                        columnspan = d.get('columnspan', 1),
                        **options)
            self.buttons.append(button)

        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def keypressed(self, key):
        print(key)
        self.processor.keyPressed(key)
        print(self.processor.getDisplay())
        self.display['text'] = self.processor.getDisplay()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)

        self.title('Calculator')
        self.geometry('300x400')
        self.configure(bg='#333')
        # self.resizable(False, False)


if __name__ == "__main__":
    app = App()
    CalculatorFrame(app)
    app.mainloop()
