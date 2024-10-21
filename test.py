# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Main Menu")
# Set geometry(widthxheight)
root.geometry('1920x1080')

menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

def clicked():

    res = "Searched: " + txt.get()
    lbl.configure(text = res)

lbl = Label(root, text = "Search by tail number: ")
lbl.grid()

txt = Entry(root, width=10)
txt.grid(column =1, row =0)

btn = Button(root, text = "Search", fg = "red", command=clicked)
btn.grid(column=2, row=0)

root.mainloop()