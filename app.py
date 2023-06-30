from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("at-to-mass-Converter")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe1 = ttk.Frame(root, padding="3 3 12 12")
mainframe1.grid(column=0, row=0, sticky=(N,W,E,S))

mainframe2 = ttk.Frame(root, padding="3 3 12 12")
mainframe2.grid(column=0, row=0, sticky=(N,W,E,S))

dict1 = {
    0: "Zr",
    1: "Cu",
    2: "Al", 
    3: "Ni", 
    4: "Ag", 
    5: "Fe", 
    6: "Si", 
    7: "Sn", 
    8: "B", 
    9: "C", 
    10: "P", 
    11: "Y", 
    12: "Co", 
    13: "Mn", 
    14: "V", 
    15: "Ca", 
    16: "Nb", 
    17: "Cr", 
    18: "Mo", 
    19: "Ga", 
    20: "La", 
    21: "Nd", 
    22: "Ti", 
    23: "W"
}

choices = ["Zr", "Cu", "Al", "Ni", "Ag", "Fe", "Si", "Sn", "B", "C", "P", "Y", "Co", "Mn", "V", "Ca", "Nb", "Cr", "Mo", "Ga", "La", "Nd", "Ti", "W"]
choicesvar = StringVar(value=choices)

def whatsSelected():
    try:
        # print(dict1[elList.curselection()[0]])
        if len(elList.curselection()) < 2:
            messagebox.showinfo(message='Please choose at least two elements')
            return
        
        
        mainframe2.tkraise()

        for i, item in enumerate(elList.curselection()):
            print(dict1[item])

            lblElement = ttk.Label(mainframe2, text=dict1[item] + ": ")
            lblElement.grid(column=1, row=i+2, sticky=(E))

            tbElement = ttk.Entry(mainframe2, name="tb"+str(i), width=5)
            tbElement.grid(column=2, row=i+2, sticky=(W))

    except ValueError:
        pass

def goBack():
    try:
        mainframe1.tkraise()
    except ValueError:
        pass


# FRAME 1
elList = Listbox(mainframe1, listvariable=choicesvar, selectmode=EXTENDED)
elList.grid(column=1, row=1, sticky=(W))

ttk.Label(mainframe1, text="PRESS `CONTROL` WHEN SELECTING MULTIPLE ELEMENTS").grid(column=1, row=2, columnspan=3 ,sticky=W)

btnGoToPage2 = ttk.Button(mainframe1, text="NEXT", command=whatsSelected)
btnGoToPage2.grid(column=2, row=1, sticky=(S))

# FRAME 2

lblColumn1 = ttk.Label(mainframe2, text="Enter %at. of each element ").grid(column=1, row=1, columnspan=2 ,sticky=(W,E))

btnGoToPage1 = ttk.Button(mainframe2, text="BACK", command=goBack)
btnGoToPage1.grid(column=2, row=5, sticky=S)


# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass

# root = Tk()
# root.title("Feet to Meters")

# mainframe1 = ttk.Frame(root, padding="3 3 12 12")
# mainframe1.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# feet = StringVar()
# feet_entry = ttk.Entry(mainframe1, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))

# meters = StringVar()
# ttk.Label(mainframe1, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# ttk.Button(mainframe1, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# ttk.Label(mainframe1, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe1, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe1, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe1.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind("<Return>", calculate)

mainframe1.tkraise()
root.resizable(True, True)
root.mainloop()