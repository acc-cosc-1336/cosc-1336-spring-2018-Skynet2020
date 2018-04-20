from tkinter import Tk, Label, Frame
from converter import Converter


class Win(Tk):

    def __init__(self):
        Tk.__init__(self, None, None)
        self.wm_title('Miles to km converter')
        self.geometry('150x150')
        self.frame = Frame()
        c = Converter()
        km = 100
        self.label1 = Label(self.frame, text='Km: ' + str(km)) 
        self.label2 = Label(self.frame, text='Miles: ' + str(c.get_miles_from_km(km)))
        
        
        self.label1.pack()
        self.label2.pack()
        self.frame.pack()


        self.mainloop()


