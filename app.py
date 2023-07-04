from tkinter import *
from tkinter import ttk
from tkinter import messagebox

AVG_SIMPLIFIED = 6.02214
elList = []

root = Tk()
root.title("at-to-mass-Converter")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe1 = ttk.Frame(root, padding="3 3 12 12")
mainframe1.grid(column=0, row=0, sticky=(N,W,E,S))

mainframe2 = ttk.Frame(root, padding="3 3 12 12")
mainframe2.grid(column=0, row=0, sticky=(N,W,E,S))

class Element:
    def __init__(self, symbol, atomicWeight):
        self.symbol = symbol
        self.atomicWeight = atomicWeight

dict1 = {
    0: Element("Zr", 91.22),
    1: Element("Cu", 63.546),
    2: Element("Al", 26.98154), 
    3: Element("Ni", 58.70), 
    4: Element("Ag", 107.868), 
    5: Element("Fe", 55.847), 
    6: Element("Si", 28.0855), 
    7: Element("Sn", 118.69), 
    8: Element("B", 10.81), 
    9: Element("C", 12.011), 
    10: Element("P", 30.97376), 
    11: Element("Y", 88.9059), 
    12: Element("Co", 58.9332), 
    13: Element("Mn", 54.9380), 
    14: Element("V", 50.9415), 
    15: Element("Ca", 40.08), 
    16: Element("Nb", 92.9064), 
    17: Element("Cr", 51.996), 
    18: Element("Mo", 95.94), 
    19: Element("Ga", 69.72), 
    20: Element("La", 138.9055), 
    21: Element("Nd", 144.24), 
    22: Element("Ti", 47.90), 
    23: Element("W", 183.85)
}

choices = ["Zr", "Cu", "Al", "Ni", "Ag", "Fe", "Si", "Sn", "B", "C", "P", "Y", "Co", "Mn", "V", "Ca", "Nb", "Cr", "Mo", "Ga", "La", "Nd", "Ti", "W"]
choicesvar = StringVar(value=choices)

def whatsSelected():
    try:
        global elList
        elList = lbElements.curselection()

        if len(elList) < 2:
            messagebox.showinfo(message='Please choose at least two elements')
            return
        
        ttk.Label(mainframe2, text="Enter %at. of each element ").grid(column=1, row=1, columnspan=2 ,sticky=(W,E))

        for i, item in enumerate(elList):
            print(dict1[item].symbol)

            lblElement = ttk.Label(mainframe2, name="lbl"+str(i), text=dict1[item].symbol + ": ")
            lblElement.grid(column=1, row=i+2, sticky=W)

            tbElement = ttk.Entry(mainframe2, name="tbPrc"+str(i), width=5)
            tbElement.grid(column=1, row=i+2, sticky=E)

            tbMass = ttk.Entry(mainframe2, name="tbMass"+str(i))
            tbMass.grid(column=2, row=i+2, sticky=E)

        # BACK BUTTON
        btnBack = ttk.Button(mainframe2, text="BACK", command=goBack, name="btnBack")
        btnBack.grid(column=1, row=len(elList) + 4, sticky=W)

        # LABEL + ALLOY WEIGHT
        lblElement = ttk.Label(mainframe2, text="Enter alloy weight: ")
        lblElement.grid(column=1, row=len(elList) + 3, sticky=E)

        tbElement = ttk.Entry(mainframe2, name="tbMass", width=5)
        tbElement.grid(column=2, row=len(elList) + 3, sticky=W)

        # BTN CALCULATE
        btnCalculate = ttk.Button(mainframe2, text="CALCULATE", command=calculate, name="btnCalculate")
        btnCalculate.grid(column=2, row=len(elList) + 4, sticky=E)

        mainframe2.tkraise()

    except ValueError:
        pass

def goBack():
    try:

        for child in mainframe2.winfo_children(): 
            child.destroy()
        mainframe1.tkraise()

    except ValueError:
        pass

def calculate():
    global elList
    controlSum = 0

    sampleMass = mainframe2.nametowidget("tbMass").get()

    if not sampleMass.isnumeric():
        messagebox.showinfo(message='Please enter the sample mass')
        return
    
    sampleMass = float(sampleMass)

    for i, item in enumerate(elList):
        atInput = mainframe2.nametowidget("tbPrc"+str(i)).get()

        if not atInput.isnumeric():
            messagebox.showinfo(message='Please fill out the form')
            return

        atInput = float(atInput)
        controlSum = controlSum + (atInput * dict1[item].atomicWeight) / AVG_SIMPLIFIED

    for i, item in enumerate(elList):
        
        atInput = float(mainframe2.nametowidget("tbPrc"+str(i)).get())
        answer = round(atInput * dict1[item].atomicWeight / AVG_SIMPLIFIED  / controlSum * sampleMass, 4)
        mainframe2.nametowidget("tbMass"+str(i)).insert(0, str(answer))


# FRAME 1
lbElements = Listbox(mainframe1, listvariable=choicesvar, selectmode=EXTENDED, name="lbElements")
lbElements.grid(column=1, row=1, sticky=(W))

ttk.Label(mainframe1, text="PRESS `CONTROL` WHEN SELECTING MULTIPLE ELEMENTS").grid(column=1, row=2, columnspan=3 ,sticky=W)

btnGoToPage2 = ttk.Button(mainframe1, text="NEXT", command=whatsSelected)
btnGoToPage2.grid(column=2, row=1, sticky=(E, S))

for child in mainframe1.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

mainframe1.tkraise()
root.mainloop()