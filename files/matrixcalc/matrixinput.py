from matrixcalc import matrixcalc
from tkinter import *

class App:

    def __init__(self, m, n):
        self.root = Tk()  
        self.matrix = None
        self.entry_list = []
    
        self.frame = Frame(self.root)
        self.frame.grid()

        self.m = m
        self.n = n

        self.submit = Button(
            self.frame, text="Submit", command=self.interpret
            )
        self.submit.grid(row=500, columnspan=1000)

        self.entries(m, n)

        self.root.mainloop()

    def add_entry(self, m, n):
        entry = Entry(self.frame, width=3)
        self.entry_list.append(entry)
        entry.grid(row=m, column=n)

    def entries(self, m, n):
        for row in range(1, m+1):
            for col in range(n):
                self.add_entry(row, col)

    def interpret(self):
        x = 0
        values = []
        a = matrixcalc.matrix()

        for elem in self.entry_list:
            values.append(int(elem.get()))

        for r in range(self.m):
            row = []
            for c in range(self.n):
                row.append(values[c])
            matrixcalc.Matrix(a).add_row(row)
            del values[0:self.n]

        self.matrix = a
        self.root.destroy()
