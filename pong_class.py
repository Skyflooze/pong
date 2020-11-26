from tkinter import *

class Game:
    def __init__(self):
        self.pressed = {}
        self._interface()

    def start(self):
        self._animate()
        self.root.mainloop()

    def _interface(self):
        self.root = Tk()
        self.raquette1label = Label(text="score j1 :", anchor="nw")
        self.raquette2label = Label(text="score j2 :", anchor="nw")
        self.canvas = Canvas(width=1000, height=600, background="black")
        

        self.raquette1label.pack(side="top", fill="x")
        self.raquette2label.pack(side="top", fill="x")
        self.canvas.pack(side="top", fill="both", expand="true")

        self.barre_milieu = Barre(self.canvas, tag="barre_milieu", color="white", x=500, y=280)
        self.bord_haut = Bord(self.canvas, tag="bord_haut", color="green", x=220, y=10)
        self.bord_bas = Bord(self.canvas, tag="bord_bas", color="green", x=220, y=613)
        self.raquette1 = Raquette(self.canvas, tag="raquette1", color="white", x=15 , y=280)
        self.raquette2 = Raquette(self.canvas, tag="raquette2", color="white", x=1000, y=280)
        self.balle = Balle(self.canvas, tag="balle", color="red", x=510, y=280)
        
        

        self._set_bindings()

    def _animate(self):
        print(self.pressed)
        if self.pressed["z"]: 
            self.raquette1.move_up()
            self.raquette1.redraw()
        if self.pressed["s"]: 
            self.raquette1.move_down()
            self.raquette1.redraw()
        if self.pressed["o"]: 
            self.raquette2.move_up()
            self.raquette2.redraw()
        if self.pressed["l"]: 
            self.raquette2.move_down()
            self.raquette2.redraw()
        
        self.raquette2.redraw()
        self.root.after(20, self._animate)

    def _set_bindings(self):
        for char in ["z","s","o", "l"]:
            self.root.bind("<KeyPress-%s>" % char, self._pressed)
            self.root.bind("<KeyRelease-%s>" % char, self._released)
            self.pressed[char] = False

    def _pressed(self, event):
        self.pressed[event.char] = True

    def _released(self, event):
        self.pressed[event.char] = False

class Raquette:
    def __init__(self, canvas, tag, color="white", x=0, y=0):
        self.canvas = canvas
        self.tag = tag
        self.x = x
        self.y = y
        self.color = color
        self.redraw()

    def move_up(self):
        self.y = max(self.y -5, 30)

    def move_down(self):
        self.y = min(self.y + 5, 523)

    def redraw(self):
        x0 = self.x - 10
        x1 = self.x - 3
        y0 = self.y - 20
        y1 = self.y + 70
        self.canvas.delete(self.tag)
        self.canvas.create_rectangle(x0,y0,x1,y1,tags=self.tag, fill=self.color)

class Balle:
    def __init__(self, canvas, tag, color="red", x=0, y=0):
        self.canvas = canvas
        self.tag = tag
        self.x = x
        self.y = y
        self.color = color
        self.redraw()
        bx = 0
        by = 0

    def redraw(self):
        x0 = self.x - 20
        x1 = self.x
        y0 = self.y - 10
        y1 = self.y + 10
        self.canvas.delete(self.tag)
        self.canvas.create_oval(x0,y0,x1,y1,tags=self.tag, fill=self.color)


class Barre:
    def __init__(self, canvas, tag, color="white", x=0, y=0):
        self.canvas = canvas
        self.tag = tag
        self.x = x
        self.y = y
        self.color = color
        self.redraw()

    def redraw(self):
        x0 = self.x - 5
        x1 = self.x + 5
        y0 = self.y - 350
        y1 = self.y + 350
        self.canvas.delete(self.tag)
        self.canvas.create_rectangle(x0,y0,x1,y1,tags=self.tag, fill=self.color)

class Bord:
    def __init__(self, canvas, tag, color="green", x=0, y=0):
        self.canvas = canvas
        self.tag = tag
        self.x = x
        self.y = y
        self.color = color
        self.redraw()

    def redraw(self):
        x0 = self.x - 1000
        x1 = self.x + 1000
        y0 = self.y - 20
        y1 = self.y 
        self.canvas.delete(self.tag)
        self.canvas.create_rectangle(x0,y0,x1,y1,tags=self.tag, fill=self.color)

        
       


