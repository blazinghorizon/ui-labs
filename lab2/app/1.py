from asyncio import current_task
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk

DEFAULT_PATH = "C:\\Users\\apexk\\Downloads\\"

class Paint(object):
    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'
    flag_line = 0

    def __init__(self):
        self.root = Tk()
        self.root.title("Paint")
        self.root['bg'] = '#DDDFF2'
        self.color_history = ['#000000', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF']
        self.color_chosen = False

        self.SUBSAMPLE_VAL = 18

        self.instruments_label = ttk.Label(self.root, text='Инструменты', anchor='center', justify='center', padding=(0, 0, -10, 0), background='#DDDFF2', font=('sans-serif', 14))
        self.instruments_label.grid(row=0, column=0, columnspan=3, sticky="EW", padx=10)

        self.figures_label = ttk.Label(self.root, text='Фигуры', anchor='center', justify='center', padding=(0, 0, 0, 0), background='#DDDFF2', font=('sans-serif', 14))
        self.figures_label.grid(row=0, column=4, columnspan=3, sticky="EW", padx=10)

        self.figures_label = ttk.Label(self.root, text='Толщина', anchor='center', justify='center', padding=(0, 0, 0, 0), background='#DDDFF2', font=('sans-serif', 14))
        self.figures_label.grid(row=0, column=7, sticky="EW", padx=10)

        self.color_label = ttk.Label(self.root, text='Цвета', anchor='center', justify='center', padding=(0, 0, 0, 0), background='#DDDFF2', font=('sans-serif', 14))
        self.color_label.grid(row=0, column=9, columnspan=8, sticky="EW", padx=10)

        self.pen_pic = PhotoImage(file=DEFAULT_PATH+"pen.png").subsample(self.SUBSAMPLE_VAL, self.SUBSAMPLE_VAL)
        self.brush_pic = PhotoImage(file=DEFAULT_PATH+"brush.png").subsample(self.SUBSAMPLE_VAL, self.SUBSAMPLE_VAL)
        self.eraser_pic = PhotoImage(file=DEFAULT_PATH+"eraser.png").subsample(self.SUBSAMPLE_VAL, self.SUBSAMPLE_VAL)
        self.line_pic = PhotoImage(file=DEFAULT_PATH+"line.png").subsample(self.SUBSAMPLE_VAL, self.SUBSAMPLE_VAL)
        self.color_pic = PhotoImage(file=DEFAULT_PATH+"color-circle.png").subsample(self.SUBSAMPLE_VAL, self.SUBSAMPLE_VAL)
        self.rectangle_pic = PhotoImage(file=DEFAULT_PATH+"rounded-rectangle.png").subsample(self.SUBSAMPLE_VAL, self.SUBSAMPLE_VAL)
        self.shape_pic = PhotoImage(file=DEFAULT_PATH+"shape.png").subsample(self.SUBSAMPLE_VAL, self.SUBSAMPLE_VAL)

        self.sep_1 = ttk.Separator(self.root, orient=VERTICAL).grid(column=3, row=0, rowspan=3, sticky='wns')
        self.sep_1 = ttk.Separator(self.root, orient=VERTICAL).grid(column=7, row=0, rowspan=3, sticky='wns')
        self.sep_1 = ttk.Separator(self.root, orient=VERTICAL).grid(column=8, row=0, rowspan=3, sticky='wns')

        self.pen_button = Button(self.root, text='Карандаш', command=self.use_pen, image=self.pen_pic, state='active')
        self.pen_button.grid(row=1, column=0, padx=20, pady=10)

        self.brush_button = Button(self.root, text='Кисть', command=self.use_brush, image=self.brush_pic)
        self.brush_button.grid(row=1, column=1, padx=20, pady=10)

        self.color_button = Button(self.root, text='Цвет', command=self.choose_color, image=self.color_pic)
        self.color_button.grid(row=1, column=16, padx=20)

        self.eraser_button = Button(self.root, text='Ластик', command=self.use_eraser, padx=5, image=self.eraser_pic, anchor='center')
        self.eraser_button.grid(row=1, column=2, padx=20, pady=10)


        self.line_button = Button(self.root, text='Линия', command=self.use_line, image = self.line_pic)
        self.line_button.grid(row=1, column=4, padx=20, pady=10)
        self.line_button2 = Button(self.root, text='Квадрат', image = self.rectangle_pic)
        self.line_button2.grid(row=1, column=5, padx=20, pady=10)
        self.line_button3 = Button(self.root, text='Квадрат 2', image = self.shape_pic)
        self.line_button3.grid(row=1, column=6, padx=20, pady=10)

        var = IntVar()
        var.set(10)
        self.choose_size_button = Spinbox(self.root, from_=1, to=30, width=5, font=('sans-serif', 12), justify='center', textvariable=var)
        self.choose_size_button.grid(row=1, column=7)

        self.c = Canvas(self.root, bg='white', width=600, height=400, highlightthickness=1, highlightbackground="black")
        self.c.grid(row=2, rowspan=10, columnspan=18, sticky="NEWS", padx=1, pady=1)

        self.current_color = Button(self.root, background='#000000', width=3, relief='groove', anchor='center')
        self.current_color.grid(row=1, column=9, padx=15)

        self.alt_colors = []
        for i in range(10, 15, 1):
            current_color = Button(self.root, background='#FFFFFF', width=3, relief='groove')
            self.alt_colors.append(current_color)
            self.alt_colors[-1].grid(row=1, column=i, padx=1, pady=5)

        self.root.grid_columnconfigure(0, weight=0)
        self.root.grid_columnconfigure(1, weight=0)
        self.root.grid_columnconfigure(2, weight=0)
        self.root.grid_columnconfigure(3, weight=0)
        self.root.grid_columnconfigure(4, weight=0)
        self.root.grid_columnconfigure(5, weight=0)
        self.root.grid_columnconfigure(6, weight=0)
        self.root.grid_columnconfigure(7, weight=1)
        self.root.grid_columnconfigure(8, weight=0)
        self.root.grid_columnconfigure(9, weight=1)
        self.root.grid_columnconfigure(10, weight=0)
        self.root.grid_columnconfigure(11, weight=0)
        self.root.grid_columnconfigure(12, weight=0)
        self.root.grid_columnconfigure(13, weight=0)
        self.root.grid_columnconfigure(14, weight=0)
        self.root.grid_columnconfigure(15, weight=0)
        self.root.grid_columnconfigure(16, weight=1)
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_rowconfigure(2, weight=1)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
        self.activate_button(self.pen_button)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]
        self.current_color['background'] = self.color
        if self.color_chosen and self.current_color['background'] != self.color_history[-1]:
            self.color_history.pop(0)
            self.color_history.append(self.color)
            print(self.color_history)
            for i in range(0, 5, 1):
                self.alt_colors[i]['background'] = self.color_history[4 - i]
        elif not self.color_chosen:
            self.color_history.pop(0)
            self.color_history.append(self.color)
        self.color_chosen = True
                

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def use_line(self):
        self.activate_button(self.line_button)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color

        if self.old_x and self.old_y:
            if self.active_button == self.line_button and self.line != None:
                self.c.coords(self.line, self.c.coords(self.line)[0], self.c.coords(self.line)[1], event.x, event.y)
            else:
                self.line = self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y


    def reset(self, event):
        self.old_x, self.old_y = None, None
        self.line = None

if __name__ == '__main__':
    Paint()