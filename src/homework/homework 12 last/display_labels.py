from tkinter import Label, Frame, Entry
from converter import Converter


class DisplayLabels:

    def __init__(self):
        km = 100
        self.frame = Frame()
        self.c = Converter()
        self.label1 = Label(self.frame, text='Km: ' + str(km))
        self.label2 = Label(self.frame, text='Miles: ' + str(self.c.get_miles_from_km(km)))
        self.label1.pack(side='left')
        self.label2.pack(side='left')
        self.frame.pack()
