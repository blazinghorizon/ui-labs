from tkinter import *
from tkinter import ttk
import locale

from numpy import take

print(locale.getlocale())

root = Tk()
root.title("UI 1.3")
        
# stringvars for values
value = StringVar()
farenheit = StringVar()
celcius = StringVar()

def calculate(var, index, mode):
    print(value.get())
    farenheit.set(value.get())
    celcius.set(value.get())
    pass

value.trace("w", callback=calculate)

# create a subwindow inside the main window with paddings
content = ttk.Frame(root, padding=(3,3,12,12))
content.grid(column=0, row=0, sticky=(N, S, E, W))

# create labels for text
value_label=ttk.Label(content, text="Введите значение:")
farenheit_label = ttk.Label(content, text="Из Фаренгейта в Цельсия:")
celcius_label = ttk.Label(content, text="Из Цельсия в Фаренгейт:")

# 0-1 row <center>Label + Entry<center>

# 2 row <left>Label + Label<left> <right>Label+Label<right>
# 3 row <left>Label + Label<left> <right>Label+Label<right>

# place labels on the grid
value_label.grid(row=0, column=0, sticky="news")
farenheit_label.grid(row=1, column=0, sticky="news")
celcius_label.grid(row=2, column=0, sticky="news")

value_entry = ttk.Entry(content, textvariable=value, takefocus=1)
farenheit_entry = ttk.Entry(content, textvariable=farenheit, takefocus=0)
#farenheit_dependency = ttk.Entry(content, textvariable=farenheit_2row, takefocus=0)
celcius_entry = ttk.Entry(content, textvariable=celcius, takefocus=0)
#celcius_dependency = ttk.Entry(content, textvariable=celcius_2row, takefocus=0)

# place entries on the grid
value_entry.grid(row=0,column=1, padx=3, pady=3, sticky="ew")
farenheit_entry.grid(row=1,column=1, padx=3, pady=3, sticky="ew")
#farenheit_dependency.grid(row=3,column=1, padx=3, pady=3, sticky="ew")
celcius_entry.grid(row=2,column=1, padx=3, pady=3, sticky="ew")
#celcius_dependency.grid(row=3,column=2, padx=3, pady=3, sticky="ew")

# configure root and content for dynamic resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

content.columnconfigure(0, weight=0)
content.columnconfigure(1, weight=1)
content.rowconfigure(0, weight=1)
content.rowconfigure(1, weight=1)
content.rowconfigure(2, weight=1)

# set minsize for window
root.update()
root.minsize(root.winfo_width()-75, root.winfo_height())
root.mainloop()