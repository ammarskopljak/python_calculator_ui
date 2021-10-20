import math
import tkinter as tk
from tkinter import *

class Calc:

    def __init__(self, master):
        self.master = master
        master.wm_title('Nigga calc')
        master.geometry('250x250')

        self.textbox = Label(
            master, 
            width = 44, 
            height = 2, 
            bg = 'lightblue',
            font = ('Arial', 12),
            text = 'equasion'
            ).grid(column = 0, row = 0, columnspan = 8, sticky = 'nswe')

        self.b7 = Button(
            master,
            width = 8,
            height = 2,
            bg = 'lightgray',
            text = '7',
            font = ('Arial', 8)
            ).grid(column = 0, row = 1, sticky = 'nswe')

        self.b8 = Button(
            master,
            width = 8,
            height = 2,
            bg = 'lightgray',
            text = '8',
            font = ('Arial', 8)
            ).grid(column = 1, row = 1, sticky = 'nswe')

        self.b9 = Button(
            master,
            width = 8,
            height = 2,
            bg = 'lightgray',
            text = '9',
            font = ('Arial', 8)
            ).grid(column = 2, row = 1, sticky = 'nswe')

        self.b4 = Button(
            master,
            width = 8,
            height = 2,
            bg = 'lightgray',
            text = '4',
            font = ('Arial', 8)
            ).grid(column = 0, row = 2, sticky = 'nswe')

        self.b5 = Button(
            master,
            width = 8,
            height = 2,
            bg = 'lightgray',
            text = '6',
            font = ('Arial', 8)
            ).grid(column = 1, row = 2, sticky = 'nswe')

        self.b6 = Button(
            master,
            width = 8,
            height = 2,
            bg = 'lightgray',
            text = '6',
            font = ('Arial', 8)
            ).grid(column = 2, row = 2, sticky = 'nswe')

        self.b1 = Button(
            master,
            width = 8,
            height = 2,
            bg = 'lightgray',
            text = '1',
            font = ('Arial', 8)
            ).grid(column = 0, row = 3, sticky = 'nswe')

        self.b2 = Button(
            master,
            width = 8,
            height = 2,
            bg = 'lightgray',
            text = '2',
            font = ('Arial', 8)
            ).grid(column = 1, row = 3, sticky = 'nswe')

        self.b3 = Button(
            master,
            width = 8,
            height = 2,
            bg = 'lightgray',
            text = '3',
            font = ('Arial', 8)
            ).grid(column = 2, row = 3, sticky = 'nswe')

        self.b0 = Button(
            master,
            width = 8,
            height = 2,
            bg = 'lightgray',
            text = '0',
            font = ('Arial', 8)
            ).grid(column = 1, row = 4, sticky = 'nswe')

        self.bdot = Button(
            master,
            width = 8,
            height = 2,
            bg = 'lightgray',
            text = '.',
            font = ('Arial', 8)
            ).grid(column = 0, row = 4, sticky = 'nswe')

        self.bplus = Button(
            master,
            width = 8,
            height = 2,
            bg = 'lightgray',
            text = '+',
            font = ('Arial', 8)
            ).grid(column = 2, row = 4, sticky = 'nswe')


        self.bdel = Button(
            master,
            width = 8,
            height = 2,
            bg = 'lightgray',
            text = '<-',
            font = ('Arial', 8)
            ).grid(column = 4, row = 1, sticky = 'nswe')

        self.bdivide = Button(
            master,
            width = 8,
            height = 2,
            bg = 'lightgray',
            text = '/',
            font = ('Arial', 8)
            ).grid(column = 4, row = 2, sticky = 'nswe')

        self.bmultiply = Button(
            master,
            width = 8,
            height = 2,
            bg = 'lightgray',
            text = '*',
            font = ('Arial', 8)
            ).grid(column = 4, row = 3, sticky = 'nswe')

        self.bminus = Button(
            master,
            width = 8,
            height = 2,
            bg = 'lightgray',
            text = '-',
            font = ('Arial', 8)
            ).grid(column = 4, row = 4, sticky = 'nswe')

        main.grid_columnconfigure(0, weight=3)
        main.grid_columnconfigure(1, weight=3)
        main.grid_columnconfigure(2, weight=3)
        main.grid_columnconfigure(3, weight=3)

        


main = tk.Tk()
mainCalc = Calc(main)
main.mainloop()