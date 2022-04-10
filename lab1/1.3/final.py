# row0 label+entry
# row1 names (f, c, k)
# row2-3 table
from tkinter import *
from tkinter import ttk
import locale
import re

# set user system's locale for decimal point character
locale.setlocale(locale.LC_NUMERIC, '')
print(f"User's locale: {locale.getlocale(locale.LC_NUMERIC)[0]}")

# set different locale
locale.setlocale(locale.LC_NUMERIC, 'es_ES')
print(f"Set ESP locale: {locale.getlocale(locale.LC_NUMERIC)[0]}")

root = Tk()
root.title("UI 1.3")
        
# stringvars for values
value = StringVar()
farenheit = StringVar()
celcius = StringVar()
error_msg = StringVar()

# func - tries to parse value and sets farenheit, celcius
def parse_and_set():
    val = value.get()
    # "block" typing multiple "-" characters
    if str.startswith(val, "-"):
        if len(val) > 1:
            value.set("-" + str.replace(val[1:], "-", ""))

    # delocalize input and try to parse it
    c = (locale.delocalize(value.get()))
    try:
        float_c = float(c)
        print(f"Read number: {float_c}")
        # in case input is float, there is no error
        error_msg.set("")
    except:
        # empty line is non-convertable to string, but is not an error
        if error_msg.get().count == 0:
            print("empty")
            error_msg.set("")
            return
        # same with "-" character
        if value.get() == "-":
            print("used -")
            error_msg.set("")
            return
        # finally, input is not a number, set message
        error_msg.set("Введеные данные некорректны!")
        print(f'Input is not a number! ({value.get()})')
        return

    # if parsed to float - set two entries
    farenheit.set("{0:.2f}".format(float(c) * 9 / 5 - 32))
    celcius.set("{0:.2f}".format((float(c) - 32) * 5 / 9)) 

# func - checks input value
def check_input():
    # case with empty value
    if len(value.get()) == 0:
        error_msg.set("")
        farenheit.set("")
        celcius.set("")
    # other cases
    else:
        parse_and_set()

# callback func for value 
def calculate(var, index, mode):
    check_input()

# on every value's update call calculate func
value.trace("w", callback=calculate)

# create a subwindow inside the main window with paddings
content = ttk.Frame(root, padding=(3,3,8,12))
content.grid(column=0, row=0, sticky=(N, S, E, W))

# create labels for text
farenheit_label = ttk.Label(content, text="Из F в C:", anchor='center')
celcius_label = ttk.Label(content, text="Из C в F:", anchor='center')
error_label = ttk.Label(content, textvariable=error_msg, anchor='center')
value_label=ttk.Label(content, text="Значение:", anchor='center')

# place labels on the grid
value_label.grid(row=0, column=0, sticky="news")
error_label.grid(row=1, column=0, columnspan=2, sticky="news")
farenheit_label.grid(row=2, column=0, sticky="news")
celcius_label.grid(row=3, column=0, sticky="news")

# building entries
# value input entry with autofocus
value_entry = ttk.Entry(content, textvariable=value, takefocus=1)
# farenheit entry without autofocus and read-only implementation
farenheit_entry = ttk.Entry(content, textvariable=farenheit, takefocus=0)
farenheit_entry.bind("<Key>", lambda e: "break")
# celcius entry without autofocus and read-only implementation
celcius_entry = ttk.Entry(content, textvariable=celcius, takefocus=0)
celcius_entry.bind("<Key>", lambda e: "break")

# place entries on the grid
value_entry.grid(row=0,column=1, padx=3, pady=3, sticky="ew")
farenheit_entry.grid(row=2,column=1, padx=3, pady=3, sticky="ew")
#farenheit_dependency.grid(row=3,column=1, padx=3, pady=3, sticky="ew")
celcius_entry.grid(row=3,column=1, padx=3, pady=3, sticky="ew")
#celcius_dependency.grid(row=3,column=2, padx=3, pady=3, sticky="ew")

# configure root and content for dynamic resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=0)
content.columnconfigure(1, weight=1)
content.rowconfigure(0, weight=1)
content.rowconfigure(1, weight=1)
content.rowconfigure(2, weight=1)
content.rowconfigure(3, weight=1)

# set minsize for window and update
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()