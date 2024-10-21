from tkinter import *

#create root window
root = Tk()

root.title("Maintenance Tracker")
root.geometry('1920x1080')

#i've gone ahead and stuck everything in a method even if most of these are basically stubs
#it does allow for returning from options / plane debug info to main so thats good
def load_main_menu():
    # again why am i doing this??? there has to be a better way
    for widget in root.winfo_children():
        widget.destroy()

    main_menu = Menu(root)
    file_menu = Menu(main_menu)
    file_menu.add_command(label='Options', command=open_options_window)
    main_menu.add_cascade(label='File', menu=file_menu)
    root.config(menu=main_menu)

    lbl = Label(root, text="Search by tail number: ")
    lbl.grid(column=0, row=0)

    txt = Entry(root, width=10)
    txt.grid(column=1, row=0)

    btn = Button(root, text="Search", fg="red", command=lambda: clicked(lbl, txt))
    btn.grid(column=2, row=0)

    open_window_btn = Button(root, text="N17HTD", command=open_plane_menu)
    open_window_btn.grid(column=0, row=1)

#im going to CRYYY
def open_options_window():
    new_window = Toplevel(root)
    new_window.title("Options")
    new_window.geometry('600x400')

    new_menu = Menu(new_window)
    new_item = Menu(new_menu)
    new_item.add_command(label='Save')
    new_item.add_command(label='Exit', command=new_window.destroy)
    new_menu.add_cascade(label='Options', menu=new_item)
    new_window.config(menu=new_menu)

    new_label = Label(new_window, text="You do not have sufficient access to view these options.")
    new_label.pack()

#this doesnt even do anything
def clicked(lbl, txt):
    res = "Searched: " + txt.get()
    lbl.configure(text=res)


def open_plane_menu():
    #this is probably bad
    for widget in root.winfo_children():
        widget.destroy()

    
    new_menu = Menu(root)
    plane_menu = Menu(new_menu)
    plane_menu.add_command(label='View Log', command=view_log)
    plane_menu.add_command(label='Maintenance Status', command=maintenance_status)
    plane_menu.add_command(label='Back to Main Menu', command=load_main_menu)
    plane_menu.add_command(label='Exit', command=root.quit)
    
    new_menu.add_cascade(label='Test Plane - N17HTD', menu=plane_menu)
    root.config(menu=new_menu)

    #add plane-specific content in theory
    #and even have a huge header. i love huge headers
    plane_label = Label(root, text="Plane N17HTD - Test Plane Information", font=('Comic Sans', 24))
    #WHYYY DOESNT COMIC SANS WORK
    #i have no idea if this breaks on different allignments but WHATEVERRRR 
    plane_label.pack(pady=20)

    log_button = Button(root, text="View Log", command=view_log)
    log_button.pack(pady=10)

    status_button = Button(root, text="Maintenance Status", command=maintenance_status)
    status_button.pack(pady=10)

    back_button = Button(root, text="Back to Main Menu", command=load_main_menu)
    back_button.pack(pady=10)

def view_log():
    log_window = Toplevel(root)
    log_window.title("N17HTD - Log")
    log_window.geometry('400x300')
    Label(log_window, text="Displaying log for N17HTD... Btw, this is some hardcoded nonsense. :D").pack()

def maintenance_status():
    status_window = Toplevel(root)
    status_window.title("N17HTD - Maintenance Status")
    status_window.geometry('400x300')
    Label(status_window, text="Displaying maintenance status for N17HTD... More nonesense!").pack()

load_main_menu()

root.mainloop()