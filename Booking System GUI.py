# Imports Various UI Modules
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import filedialog

# Quit Application
def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       window.destroy()
    else:
        tk.messagebox.showinfo('Return','You will now return to the application',icon = 'warning')

#Unlock Entry 
def ID_Entered():
    Nights_Enter.config(state = NORMAL)
    Member_Button.config (state = NORMAL)
    ID_Enter.config(state = DISABLED)
    Nights_Button.config(state = NORMAL)

# TK UI Ellements

# Base UI
window = Tk()
window.title("Booking System")
window.geometry('700x400')
tab_control = ttk.Notebook(window)

# Window Tabs
Member_List = ttk.Frame(tab_control)
Book_Nights = ttk.Frame(tab_control)
Management = ttk.Frame(tab_control)

# Window 1
tab_control.add(Member_List, text='Members')
tab_control.add(Book_Nights, text='Book Nights')
tab_control.add(Management
, text='Management')

# Tab 1
listbox = Listbox(Member_List, width=80, height=20, font="Monaco")
listbox.pack()
table = [["spam", 42, "test", ""],["eggs", 451, "", "we"],["bacon", "True", "", ""]]
headers = ["Surname", "Member ID", "Membership", "Points"]
row_format ="{:<10}  {:<10}  {:<10}  {:<10}"
listbox.insert(0, row_format.format(*headers, sp=" "*2))
for items in table:
    listbox.insert(END, row_format.format(*items, sp=" "*2))
scrollbar = Scrollbar(Member_List, orient="vertical")
scrollbar.config(command=listbox.yview)
scrollbar.pack(side="right", fill="y")

# Tab 2
Member_ID = Label(Book_Nights, text= 'Member ID')
Member_ID.grid(column=0, row=0)

Nights = Label(Book_Nights, text= 'Nights')
Nights.grid(column=0, row=1)

ID_Enter = tk.Entry(Book_Nights)
ID_Enter.grid(row=0, column=1)

Nights_Enter = tk.Entry(Book_Nights)
Nights_Enter.grid(row=1, column=1)

Member_Button = tk.Button(Book_Nights, text='ENTER', command=ID_Entered)
Member_Button.grid(row=0, column=2)

Nights_Button = tk.Button(Book_Nights, text='ENTER', command="")
Nights_Button.grid(row=1, column=2)

# Tab 3
Surname = Label(Management, text= 'Surname:')
Surname.grid(column=0, row=0)

Surname_Entry = tk.Entry(Management)
Surname_Entry.grid(row=0, column=1)

RLELine = tk.Button(Management, text='ENTER', command="")
RLELine.grid(row=0, column=2)

# Quit Button
Button(window, text='QUIT', fg = "Red", command=ExitApplication).pack(side=BOTTOM)

# Dissable UI Entry
Nights_Enter.config(state = DISABLED)
Nights_Button.config (state = DISABLED)
    
# Restart Entry Point
def Reset():
    Nights_Enter.delete(0, END)
    Nights_Enter.config(state = DISABLED)
    Nights_Button.config (state = DISABLED)
    ID_Enter.config(state = NORMAL)
    Nights_Button.config (state = NORMAL)
    ID_Enter.delete(0, END)
ResetButton = tk.Button(Book_Nights, text='RESET', command=Reset)
ResetButton.grid(row=0, column=5)

# Window Complete
tab_control.pack(expand=1, fill='both')
window.mainloop()
