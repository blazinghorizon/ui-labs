from tkinter import *
from tkinter import ttk
import locale
import re
import utils

# const array for converison order
ORDER = ['F', 'C', 'K']

# set user system's locale for decimal point character
locale.setlocale(locale.LC_NUMERIC, '')
print(f"User's locale: {locale.getlocale(locale.LC_NUMERIC)[0]}")

# set different locale
locale.setlocale(locale.LC_NUMERIC, 'es_ES')
print(f"Set ESP locale: {locale.getlocale(locale.LC_NUMERIC)[0]}")

# tkinter creation
root = Tk()
root.title("UI 1.4")
        
# stringvars for values
value = StringVar()
table_vars = []
for i in range(9):
    table_vars.append(StringVar())
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

    # set all entries in table
    for i in range(9):
        current_value = float(utils.converison(float_c, from_metric=ORDER[i // 3], to_metric=ORDER[i % 3]))
        table_vars[i].set("{0:.2f}".format(current_value))

# func - checks input value
def check_input():
    # case with empty value
    if len(value.get()) == 0:
        error_msg.set("")
        for var in table_vars:
            var.set("")
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
farenheit_label_top = Label(content, text="F", anchor='center')
celcius_label_top = Label(content, text="C", anchor='center')
kelvin_label_top = Label(content, text="К", anchor='center')
farenheit_label_left = Label(content, text="F", anchor='center')
celcius_label_left = Label(content, text="C", anchor='center')
kelvin_label_left = Label(content, text="К", anchor='center')
error_label = Label(content, textvariable=error_msg, anchor='center')
value_label = Label(content, text="Значение:", anchor='center')

# place labels on the grid
value_label.grid(row=0, column=0, sticky="news")
error_label.grid(row=1, column=0, columnspan=4, sticky="news")
farenheit_label_left.grid(row=3, column=0, sticky="news")
farenheit_label_top.grid(row=2, column=1, sticky="news")
celcius_label_left.grid(row=4, column=0, sticky="news")
celcius_label_top.grid(row=2, column=2, sticky="news")
kelvin_label_left.grid(row=5, column=0, sticky="news")
kelvin_label_top.grid(row=2, column=3, sticky="news")

# building entries
value_entry = ttk.Entry(content, textvariable=value, takefocus=1)
value_entry.focus_set()
table_entries = []
for i in range(9):
    #create entry and make it read-only
    paint_color = 'lightgray' if i % 4 == 0 else 'white'
    table_entries.append(Entry(content, textvariable=table_vars[i], takefocus=0, bg=paint_color))
    table_entries[i].bind("<Key>", lambda e: "break")

# place entries on the grid
value_entry.grid(row=0, column=1, columnspan=3, padx=3, pady=3, sticky="ew")
ROW_PAD = 3
COL_PAD = 1
for i in range(9):
    row_n = ROW_PAD + i // 3
    col_n = i % 3 + COL_PAD
    table_entries[i].grid(row=row_n, column=col_n, sticky="news")

# configure root and content for dynamic resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=0)
content.columnconfigure(1, weight=1)
content.columnconfigure(2, weight=1)
content.columnconfigure(3, weight=1)
content.rowconfigure(0, weight=1)
content.rowconfigure(1, weight=0)
content.rowconfigure(2, weight=1)
content.rowconfigure(3, weight=1)
content.rowconfigure(4, weight=1)
content.rowconfigure(5, weight=1)

# set minsize for window and update
root.update()
root.geometry(f'{root.winfo_width()-200}x{root.winfo_height()}')
root.minsize(root.winfo_width()-200, root.winfo_height())
root.mainloop()
