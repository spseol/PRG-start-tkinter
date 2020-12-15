#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import Scale, Canvas, Entry, HORIZONTAL, StringVar

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
        self.entryR = Entry(
            self,
            fg="#ff0000",
            textvariable=self.varR,
            validate="key",
            vcmd=(entryValidate, "%P"),
        )
        self.entryR.pack()
        self.scaleR = Scale(
            from_=0,
            to=255,
            orient=HORIZONTAL,
            command=self.change,
            background="#ff0000",
            length=self.length,
        )
        self.scaleR.pack()
        self.scaleG = Scale(
            from_=0,
            to=255,
            orient=HORIZONTAL,
            command=self.change,
            background="#00ff00",
            length=self.length,
        )
        self.scaleG.pack()
        self.scaleB = Scale(
            from_=0,
            to=255,
            orient=HORIZONTAL,
            command=self.change,
            background="#0000ff",
            length=self.length,
        )
        self.scaleB.pack()
        self.canvas = Canvas(background="#000000")
        self.canvas.pack()

        self.varColor = StringVar()
        self.entryColor = Entry(textvariable=self.varColor, width=7)
        self.entryColor.pack()

    def entryValidate(self, value):
        if value.isdigit():
            return True
        else:
            return False

    def entryUpdate(self, *arg):
        "https://stackoverflow.com/questions/29690463/what-are-the-arguments-to-tkinter-variable-trace-method-callbacks#29697307"
        "print(name, index, operation)"
        r = self.varR.get()
        """if r.isdigit():
            r = int(r)
        else:
            self.varR.set(0)
            r = 0"""
        self.scaleR.set(r)

    def change(self, event):
        r = self.scaleR.get()
        self.varR.set(r)
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
