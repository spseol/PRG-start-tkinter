#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import Scale, Canvas, Entry, HORIZONTAL, StringVar, N, S, E, W

# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "ColorMishMash"
    length = 333

    def __init__(self):
        super().__init__(className=self.name)
        entryValidate = self.register(self.entryValidate)
        self.title(self.name)
        self.bind("<Escape>", self.quit)

        self.varR = StringVar(name="varR")
        self.varR.set(0)
        self.varR.trace("w", self.entryUpdate)

        self.varG = StringVar(name="varG")
        self.varG.set(0)
        self.varG.trace("w", self.entryUpdate)

        self.varB = StringVar(name="varB")
        self.varB.set(0)
        self.varB.trace("w", self.entryUpdate)

        self.entryR = Entry(
            self,
            fg="#ff0000",
            textvariable=self.varR,
            validate="key",
            validatecommand=(entryValidate, "%P"),
            width=4,
        )
        self.entryG = Entry(
            self,
            fg="#00ff00",
            textvariable=self.varG,
            validate="key",
            validatecommand=(entryValidate, "%P"),
            width=4,
        )
        self.entryB = Entry(
            self,
            fg="#0000ff",
            textvariable=self.varB,
            validate="key",
            validatecommand=(entryValidate, "%P"),
            width=4,
        )
        self.scaleR = Scale(
            from_=0,
            to=255,
            orient=HORIZONTAL,
            command=self.change,
            variable=self.varR,
            background="#ff0000",
            length=self.length,
        )
        self.scaleR.set(55)
        self.scaleG = Scale(
            from_=0,
            to=255,
            orient=HORIZONTAL,
            command=self.change,
            variable=self.varG,
            background="#00ff00",
            length=self.length,
        )
        self.scaleB = Scale(
            from_=0,
            to=255,
            orient=HORIZONTAL,
            command=self.change,
            variable=self.varB,
            background="#0000ff",
            length=self.length,
        )
        self.canvas = Canvas(background="#000000")
        self.varColor = StringVar()
        self.entryColor = Entry(textvariable=self.varColor, width=7)

        self.scaleR.grid(row=0, column=0)
        self.entryR.grid(row=0, column=1)
        self.scaleG.grid(row=1, column=0)
        self.entryG.grid(row=1, column=1)
        self.scaleB.grid(row=2, column=0)
        self.entryB.grid(row=2, column=1)
        self.canvas.grid(row=3, column=0, sticky=E)
        self.entryColor.grid(row=3, column=1, sticky=N)

    def entryValidate(self, value):
        return value.isdigit()
        if value.isdigit():
            return True
        else:
            return False

    def entryUpdate(self, *arg):
        "https://stackoverflow.com/questions/29690463/what-are-the-arguments-to-tkinter-variable-trace-method-callbacks#29697307"
        name, index, operation = arg
        # r = self.varR.get()
        # # if r.isdigit():
        # #     r = int(r)
        # # else:
        # #     self.varR.set(0)
        # #     r = 0
        # self.scaleR.set(r)

        # g = self.varG.get()
        # self.scaleG.set(g)

    def change(self, event):
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()
        hashcolor = "#%02x%02x%02x" % (r, g, b)
        hashcolor = "#{:02x}{:02x}{:02x}".format(r, g, b)
        print(hashcolor)
        self.canvas.config(background=hashcolor)
        self.varColor.set(hashcolor)

    def quit(self, event=None):
        print(self.entryR.get())
        self.entryR.config()
        super().quit()


app = Application()
app.mainloop()
