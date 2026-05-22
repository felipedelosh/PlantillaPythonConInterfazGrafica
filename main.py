"""
FelipedelosH


This is a example of blank template
"""
from tkinter import *
from src.controllers.controller import *

class Software:
    def __init__(self) -> None:
        self.controller = Controller()
        self._w = self.controller.config._data.get("window_w")
        self._h = self.controller.config._data.get("window_h")
        self.screem = Tk()
        self.canvas = Canvas(self.screem)
        self.lblBannerProgram = Label(self.canvas, text="This is a main banner")
        self.lblFooterProgram = Label(self.canvas, text="This is a main Footer")

        # DEMO
        self._demo()
        # DEMO
        self.vizualizedAndRun()


    def vizualizedAndRun(self):
        self.screem.title(self.controller.config._data.get("title_app"))
        self.screem.geometry(f"{self._w}x{self._h}")
        self.canvas['width'] = self._w
        self.canvas['height'] = self._h
        self.canvas['bg'] = "snow"
        self.canvas.place(x=0, y=0)
        self.lblBannerProgram.place(x=20, y=20)
        self.lblFooterProgram.place(x=200, y=450)

        self.screem.after(0, self._refreshWindow)
        self.screem.mainloop()

    def _refreshWindow(self):
        self.screem.after(60, self._refreshWindow)

    def _demo(self):
        print("This is a demo app")
        print(self.controller.getTextInFile("data/arc nr1.txt"))    
        print("================")
        print(self.controller.getAllFilesNamesByExt("data", ".txt"))

s = Software()
