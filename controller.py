"""
FelipedelosH



"""

class Controller:
    def __init__(self) -> None:
        print("Gretting from Controller")
        pass

    def rtnArcheveInfo(self, path):
        info = None
        try:
            f = open(path, 'r', encoding="utf-8")
            return f.read()
        except:
            return info

        pass