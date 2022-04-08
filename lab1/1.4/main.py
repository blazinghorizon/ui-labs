# row0 label+entry
# row1 names (f, c, k)
# row2-3 table
from tkinter import *
from tkinter import ttk
import locale
import re

cur_locale = locale.getlocale()

locale.setlocale(locale.LC_NUMERIC, cur_locale)

root = Tk()
root.title("UI 1.3")
        
# stringvars for values
value = StringVar()
farenheit = StringVar()
celcius = StringVar()
error_msg = StringVar()

def parse_to_float(val):
    if str.startswith(val, "-"):
        if len(val) > 1:
            value.set("-" + str.replace(val[1:], "-", ""))
        return val

    c = (locale.delocalize(val))
    try:
        float_c = float(c)
        print(float_c)
        error_msg.set("")
    except:
        if error_msg.get().count == 0:
            print("empty")
            error_msg.set("")
            return    
        error_msg.set("Введеные данные некорректны!")
        print('exception')
        return

    farenheit.set("{0:.2f}".format(float(c) * 9 / 5 - 32))
    celcius.set("{0:.2f}".format((float(c) - 32) * 5 / 9)) 
    #print(locale.format_string("%f", value))
    #locale.delocalize()
    

def check_input(val):
    if len(val) == 0:
        error_msg.set("")
        farenheit.set("")
        celcius.set("")
        return
    else:
        parsed = parse_to_float(val)
                

def calculate(var, index, mode):
    if not check_input(value.get()):
        return
    farenheit.set(value.get())
    celcius.set(value.get())
    pass

value.trace("w", callback=calculate)

# create a subwindow inside the main window with paddings
content = ttk.Frame(root, padding=(3,3,8,12))
content.grid(column=0, row=0, sticky=(N, S, E, W))

# create labels for text
farenheit_label = ttk.Label(content, text="Из F в C:", anchor='center')
celcius_label = ttk.Label(content, text="Из C в F:", anchor='center')
error_label = ttk.Label(content, textvariable=error_msg)
value_label=ttk.Label(content, text="Значение:", anchor='center')
# 0-1 row <center>Label + Entry<center>

# 2 row <left>Label + Label<left> <right>Label+Label<right>
# 3 row <left>Label + Label<left> <right>Label+Label<right>

# place labels on the grid
value_label.grid(row=0, column=0, sticky="news")
error_label.grid(row=1, column=0, columnspan=2, sticky="news")
farenheit_label.grid(row=2, column=0, sticky="news")
celcius_label.grid(row=3, column=0, sticky="news")

value_entry = ttk.Entry(content, textvariable=value, takefocus=1)
farenheit_entry = ttk.Entry(content, textvariable=farenheit, takefocus=0)
#farenheit_dependency = ttk.Entry(content, textvariable=farenheit_2row, takefocus=0)
celcius_entry = ttk.Entry(content, textvariable=celcius, takefocus=0)
#celcius_dependency = ttk.Entry(content, textvariable=celcius_2row, takefocus=0)

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

# set minsize for window
root.update()
root.minsize(root.winfo_width()-75, root.winfo_height())
root.mainloop()