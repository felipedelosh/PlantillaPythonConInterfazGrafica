"""
FelipedelosH

"""
import re
from tkinter import *
from controller import *

class Software:
    def __init__(self) -> None:
        self.controller = Controller()
        self.screem = Tk()
        self.canvas = Canvas(self.screem)
        self.lblBannerProgram = Label(self.canvas, text="This is a main banner")
        self.lblFooterProgram = Label(self.canvas, text="This is a main Footer")


        self.vizualizedAndRun()


    def vizualizedAndRun(self):
        self.screem.title("Program Title")
        self.screem.geometry("720x480")
        self.canvas['width'] = 720
        self.canvas['height'] = 480
        self.canvas['bg'] = "snow"
        self.canvas.place(x=0, y=0)
        self.lblBannerProgram.place(x=20, y=20)
        self.lblFooterProgram.place(x=200, y=450)


        print(self.rtnArcheveInfo("archive.txt"))    

        self.screem.mainloop()

    def rtnArcheveInfo(self, path):
        info = None
        try:
            f = open(path, 'r', encoding="utf-8")
            return f.read()
        except:
            return info

        pass


s = Software()