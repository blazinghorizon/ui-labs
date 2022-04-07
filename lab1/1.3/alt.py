from tkinter import *
from tkinter import ttk

history = []

# conversion function
def calculate():
    is_farenheit_empty = False
    is_celcius_empty = False

    farenheit_value = farenheit.get()
    celcius_value = celcius.get()
    history.append([farenheit_value, celcius_value])

    if farenheit_value == "":
        is_farenheit_empty = True

    if celcius_value == "":
        is_celcius_empty = True

    if is_farenheit_empty and not is_celcius_empty:
        farenheit.set("{0:.2f}".format(float(celcius_value) * 1.8 + 32))

    if not is_farenheit_empty and is_celcius_empty:
        celcius.set("{0:.2f}".format((float(farenheit_value) - 32) * 5 / 9))

    return

        
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

def callback(value):
    if value == 1:
        farenheit_value = farenheit.get()
        if not farenheit_value or farenheit_value.isspace():
            celcius.set("")
        #celcius.set("{0:.2f}".format((float(farenheit_value) - 32) * 5 / 9))
        celcius.set((float(farenheit_value) - 32) * 5 / 9)

    if value == 2:
        celcius_value = celcius.get()
        if not celcius_value.strip():
            farenheit.set("")
        #farenheit.set("{0:.2f}".format(float(celcius_value) * 1.8 + 32))
        farenheit.set(float(celcius_value) * 1.8 + 32)

last_updated_entry = 0
last_farenheit_value = 0.0
last_celcius_value = 0.0

root = Tk()
root.title("UI 1.1")

# stringvars for values
farenheit = StringVar()
celcius = StringVar()

farenheit.trace("w", lambda name, index, mode, farenheit=farenheit: callback(1))
celcius.trace("w", lambda name, index, mode, celcius=celcius: callback(2))

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
celcius_entry = ttk.Entry(content, textvariable=celcius, takefocus=1)

# place entries on the grid
farenheit_entry.grid(row=0,column=1, padx=3, pady=3, sticky="ew")
celcius_entry.grid(row=1,column=1, padx=3, pady=3, sticky="ew")

magic_button = ttk.Button(content, text="Очистить", command=clear_entires, takefocus=1)
magic_button.grid(row=0,column=2, rowspan=2, padx=0, pady=0, sticky="ew")

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