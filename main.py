from random import randint

class Button():
    def __init__(self, btext, bdescription, bvolume, x, y):
        self.btext = btext
        self.bdescription = bdescription
        self.x = x
        self.y = y
        self.boole = True
    def hide(self):
        self.boole = False
    def show(self):
        self.boole = True
    def printinfo(self):
        print(self.btext)
        print(self.bdescription)
        print(self.boole)

b1 = Button("Text", "Description", 1, 1, 1, )
b1.hide()
b1.printinfo()
b1.show()
b1.printinfo()