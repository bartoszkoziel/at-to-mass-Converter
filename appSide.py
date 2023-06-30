import tkinter as tk
from tkinter import *

root = tk.Tk()

page1 = tk.Frame(root)
page2 = tk.Frame(root)

page1.grid(row=0, column=0)
page2.grid(row=0, column=0)

lbl1 = tk.Label(page1, text="GAPGE 1")
lbl2 = tk.Label(page2, text="GAPGE 2")


root.geometry("650x650")
root.title("test")
root.resizable(False, False)
root.mainloop()