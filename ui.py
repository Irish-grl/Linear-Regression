
from tkinter import *
from tkinter import ttk


class UI:

   def __init__(self, root):

        root.title("Retirement Savings Estimator")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        age = IntVar()
        age = ttk.Entry(mainframe, width=7, textvariable=age)
        age.grid(column=2, row=1, sticky=(W, E))
        ttk.Label(mainframe, text ="Enter your age: ").grid(column=1, row=1, sticky=(W, E))

        yearly_salary = StringVar()
        yearly_salary = ttk.Entry(mainframe, width=7, textvariable=yearly_salary)
        yearly_salary.grid(column=2, row=2, sticky=(W, E))
        ttk.Label(mainframe, text="Enter your gross yearly wages: ").grid(column=1, row=2, sticky=(W, E))

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        ttk.Label(mainframe, text="Press the Calculate button to get your estimate: ").grid(column=1, row=3, sticky=(W, E))
        ttk.Button(mainframe, text="Calculate Amount to Save").grid(column=2, row=3, sticky=(W, E))
        age.focus()

        #root.bind("<Enter>", calculate)

    #def calculate(self):


root = Tk()
UI(root)
root.mainloop()

