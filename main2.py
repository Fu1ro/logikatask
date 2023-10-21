from random import randint

class Button():
    def __init__(self, btext, x, y):
        self.btext = btext
        self.x = x
        self.y = y
        self.boole = True
    def printinfo(self):
        print("Кнопка:", self.btext)
        print(f"Розташування: ({self.x}, {self.y})")
        print("Видимість: ", self.boole)
    def hide(self):
        self.boole = False
        print(self.btext, " - приховано")
    def show(self):
        self.boole = True
        print(self.btext, " - відображено")

b1 = Button("Дізнатися переможця прямо зараз!", 150, 50)
b2 = Button("Переможець може бути тільки один", 150, -100)

b2.hide()
b1.printinfo()
b2.printinfo()