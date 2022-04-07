from tkinter import *
from tkinter import ttk

# conversion function
def calculate():
    current_value = farenheit.get()
    if current_value == "":
        return
    celcius.set("{0:.2f}".format((float(current_value) - 32) * 5 / 9))

# validation function
def test_val(inStr, acttyp):
    if acttyp == '1':
        if not is_float(inStr):
            return False
    return True

# check if value is convertable to float
def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

root = Tk()
root.title("UI 1.1")

# stringvars for values
farenheit = StringVar()
celcius = StringVar()

# create a subwindow inside the main window with paddings
content = ttk.Frame(root, padding=(3,3,12,12))
content.grid(column=0, row=0, sticky=(N, S, E, W))

# create two labels for text
farenheit_label = ttk.Label(content, text="Градусы Фаренгейта:")
celcius_label = ttk.Label(content, text="Градусы Цельсия:")

# place labels on the grid
farenheit_label.grid(row=0, column=0, sticky="news")
celcius_label.grid(row=1, column=0, sticky="news")
 
# create farenheit entry
farenheit_entry = ttk.Entry(content, textvariable=farenheit, validate="key")
# bind validatecommand to block user from typing non-numeric symbols
farenheit_entry['validatecommand'] = (farenheit_entry.register(test_val),'%P','%d')

# create celcius entry
celcius_entry = ttk.Entry(content, textvariable=celcius)
# bind any key press to a function that returns "break" to make entry read-only
celcius_entry.bind("<Key>", lambda e: "break")

# place entries on the grid
farenheit_entry.grid(row=0,column=1, padx=3, pady=3, sticky="ew")
celcius_entry.grid(row=1,column=1, padx=3, pady=3, sticky="ew")

# create button
magic_button = ttk.Button(content, text="Преобразовать", command=calculate)
magic_button.grid(row=0,column=2, padx=0, pady=0, sticky="ew")

# configure root and content for dynamic resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=0)
content.columnconfigure(1, weight=1)
content.columnconfigure(2, weight=0)
content.rowconfigure(0, weight=1)
content.rowconfigure(1, weight=1)

# set minsize for window
root.update()
root.minsize(root.winfo_width()-75, root.winfo_height())
root.mainloop()