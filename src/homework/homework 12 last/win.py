from tkinter import Tk, Button, Frame
from display_labels import DisplayLabels


class Win(Tk):

    def __init__(self):
        Tk.__init__(self, None, None)
        self.wm_title('Miles to km converter')
        self.geometry('320x90')
        self.frame = Frame()
        self.my_button = Button(self.frame, text='Display conversion', command=DisplayLabels)
        self.quit_button = Button(self.frame, text='Quit', command=self.destroy)
        self.my_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.frame.pack(side='bottom')

        self.mainloop()
