from tkinter import *
from tkinter import ttk
from tkinter import messagebox

AVG_SIMPLIFIED = 6.02214
tempvar = 0

root = Tk()
root.title("at-to-mass-Converter")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe1 = ttk.Frame(root, padding="3 3 12 12", width=200, height=100)
mainframe1.grid(column=0, row=0, sticky=(N,W,E,S))

mainframe2 = ttk.Frame(root, padding="3 3 12 12", width=100, height=100)
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
        global tempvar
        tempvar = elList.curselection()
        tabTamp = elList.curselection()
        print("TEB_TEMP: ", tabTamp)

        if len(elList.curselection()) < 2:
            messagebox.showinfo(message='Please choose at least two elements')
            return
        
        ttk.Label(mainframe2, text="Enter %at. of each element ").grid(column=1, row=1, columnspan=2 ,sticky=(W,E))

        for i, item in enumerate(elList.curselection()):
            print(dict1[item].symbol)

            lblElement = ttk.Label(mainframe2, name="lbl"+str(i), text=dict1[item].symbol + ": ")
            lblElement.grid(column=1, row=i+2, sticky=W)

            tbElement = ttk.Entry(mainframe2, name="tbPrc"+str(i), width=5)
            tbElement.grid(column=1, row=i+2, sticky=E)

            tbMass = ttk.Entry(mainframe2, name="tbMass"+str(i))
            tbMass.grid(column=2, row=i+2, sticky=E)

        # BACK BUTTON
        btnBack = ttk.Button(mainframe2, text="BACK", command=goBack, name="btnBack")
        btnBack.grid(column=1, row=len(elList.curselection()) + 4, sticky=W)

        # LABEL + ALLOY WEIGHT
        lblElement = ttk.Label(mainframe2, text="Enter alloy weight: ")
        lblElement.grid(column=1, row=len(elList.curselection()) + 3, sticky=E)

        tbElement = ttk.Entry(mainframe2, name="tbMass", width=5)
        tbElement.grid(column=2, row=len(elList.curselection()) + 3, sticky=W)

        # BTN CALCULATE
        btnCalculate = ttk.Button(mainframe2, text="CALCULATE", command=calculate, name="btnCalculate")
        btnCalculate.grid(column=2, row=len(elList.curselection()) + 4, sticky=E)

        mainframe2.tkraise()

    except ValueError:
        pass

def goBack():
    try:
        mainframe1.tkraise()

        for child in mainframe2.winfo_children(): 
            child.destroy()

    except ValueError:
        pass

def calculate():

    global tempvar

    tabHelper = tempvar

    print("TAB_HELPER: ", tabHelper)
    print("TEMPVAR: ", tempvar)
    controlSum = 0
    print("HERE: ", tabHelper)
    for i, item in enumerate(tabHelper):
        atInput = float(mainframe2.nametowidget("tbPrc"+str(i)).get())
        controlSum = controlSum + (atInput * dict1[item].atomicWeight) / AVG_SIMPLIFIED

        # print("====================")
        # print("CONTROL SUM: ", controlSum)
        # print("atInput: ", atInput)
        # print("dict1[item].atomicWeight", dict1[item].atomicWeight)
        # print("AVG_SIMPLIFIED: ", AVG_SIMPLIFIED)

    for i, item in enumerate(tabHelper):
        sampleMass = float(mainframe2.nametowidget("tbMass").get())
        atInput = float(mainframe2.nametowidget("tbPrc"+str(i)).get())
        answer = (((atInput * dict1[item].atomicWeight) / AVG_SIMPLIFIED ) / controlSum) * sampleMass
        mainframe2.nametowidget("tbMass"+str(i)).insert(0, str(answer))
    
    print(controlSum)



# FRAME 1
elList = Listbox(mainframe1, listvariable=choicesvar, selectmode=EXTENDED, name="lbElements")
elList.grid(column=1, row=1, sticky=(W))

ttk.Label(mainframe1, text="PRESS `CONTROL` WHEN SELECTING MULTIPLE ELEMENTS").grid(column=1, row=2, columnspan=3 ,sticky=W)

btnGoToPage2 = ttk.Button(mainframe1, text="NEXT", command=whatsSelected)
btnGoToPage2.grid(column=2, row=1, sticky=(E, S))


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

mainframe1.tkraise()
root.mainloop()