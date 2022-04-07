from tkinter import *
from tkinter import ttk

# conversion function
def calculate():
    current_value = farenheit.get()
    if current_value == "":
        celcius.set("0")
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

def clear_entires():
    celcius.set("")
    farenheit.set("")

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
 
# create farenheit entry with enabled tab
farenheit_entry = ttk.Entry(content, textvariable=farenheit, validate="key", takefocus=1)
# bind validatecommand to block user from typing non-numeric symbols
farenheit_entry['validatecommand'] = (farenheit_entry.register(test_val),'%P','%d')
# set autofocus
farenheit_entry.focus_set()

# create celcius entry with disabled tab
celcius_entry = ttk.Entry(content, textvariable=celcius, takefocus=0)
# bind any key press to a function that returns "break" to make entry read-only
celcius_entry.bind("<Key>", lambda e: "break")

# place entries on the grid
farenheit_entry.grid(row=0,column=1, padx=3, pady=3, sticky="ew")
celcius_entry.grid(row=1,column=1, padx=3, pady=3, sticky="ew")

# create button with enabled tab
magic_button = ttk.Button(content, text="Преобразовать", command=calculate, takefocus=1)
magic_button.grid(row=0,column=2, padx=0, pady=0, sticky="ew")

# create clear button with enabled tab
magic_button = ttk.Button(content, text="Очистить", command=clear_entires, takefocus=1)
magic_button.grid(row=1,column=2, padx=0, pady=0, sticky="ew")

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