from tkinter import *

class Game:
    def __init__(self): #Initialisation, place l'interface.
        self.pressed = {}
        self._interface()

    def start(self): #lance les mouvements des raquettes
        self._animate()
        self.root.mainloop()

    def _interface(self): #défini l'interface du jeu, c'est à dire les canvas et la fenêtre.
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

    def _animate(self): #Déplacement des raquettes
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

    def _set_bindings(self): #défini les touches de jeu
        for char in ["z","s","o", "l"]:
            self.root.bind("<KeyPress-%s>" % char, self._pressed)
            self.root.bind("<KeyRelease-%s>" % char, self._released)
            self.pressed[char] = False

    def _pressed(self, event): #Si une touche est appuyée, renvoie True pour celle-ci.
        self.pressed[event.char] = True

    def _released(self, event): #si la touche est ensuite relachée alors elle renvoie false.
        self.pressed[event.char] = False

'''
C'est dans Class Game que se trouvera les mecanismes du jeu. 
à l'initiation, _interface(self) va mettre en place la fenêtre du jeu, les canvas, c'est-à-dire
celui de la balle, ceux des raquettes, celui de la barre du milieu, leurs positions.
_animate(self) est derrière ce qui concerne le mouvement des barres, en changeant les coordonées et en les 
redessinants. Cela fonctionne avec un système de True et de False défini avec l'aide de _set_bindings(self),
_pressed(self,event) et _released.
Lorsque l'une des touches utilisées dans _set_bindings est appuyée, alors le programme va le renvoyer true dans _animate
grâce à la définition de _pressed, et va alors effectuer l'action correspondante(monter ou descendre les coordonées et
redessiner le canvas).
'''


class Raquette: 
    def __init__(self, canvas, tag, color="white", x=0, y=0): #Défini les attribus des raquettes lorsque la classe est appelée à l'initialisation du jeu
        self.canvas = canvas
        self.tag = tag
        self.x = x
        self.y = y
        self.color = color
        self.redraw()

    def move_up(self): #monte les coordonnées
        self.y = max(self.y -5, 30)

    def move_down(self): #descends les coordonnées
        self.y = min(self.y + 5, 523)

    def redraw(self): #redessine la raquette
        x0 = self.x - 10
        x1 = self.x - 3
        y0 = self.y - 20
        y1 = self.y + 70
        self.canvas.delete(self.tag)
        self.canvas.create_rectangle(x0,y0,x1,y1,tags=self.tag, fill=self.color)

'''
Création des raquettes, avec __init__ qui va être appelé au lancement du jeu pour placer les canvas déssinés
à leurs coordonnés.
move_up et move_down permettent respectivement la montée et la descente, en déplaçant les coordonées de l'axe y.
redraw supprime le canvas pour ensuite le redessiner aux nouveaux coordonnés (move_up/move_down et redraw sont 
toujours appelés ensembles dans _animate)
'''

class Balle:
    def __init__(self, canvas, tag, color="red", x=0, y=0): #défini les attribus de la balle lorsque la classe est appelée à l'initialisation du jeu
        self.canvas = canvas
        self.tag = tag
        self.x = x
        self.y = y
        self.color = color
        self.redraw()
        bx = 0
        by = 0

    def redraw(self): #redessine la balle aux nouveaux coordonnées 
        x0 = self.x - 20
        x1 = self.x
        y0 = self.y - 10
        y1 = self.y + 10
        self.canvas.delete(self.tag)
        self.canvas.create_oval(x0,y0,x1,y1,tags=self.tag, fill=self.color)

'''
Définition des attribus de la balle, et de redraw permettant à la balle d'être redessinée à chaque fois que ses 
coordonnées vont se modifier.
'''



class Barre:  
    def __init__(self, canvas, tag, color="white", x=0, y=0): #défini les attribus de la barre, puis la dessine lorsque le jeu est initialisé
        self.canvas = canvas
        self.tag = tag
        self.x = x
        self.y = y
        self.color = color
        self.redraw()

    def redraw(self): #dessine la barre
        x0 = self.x - 5
        x1 = self.x + 5
        y0 = self.y - 350
        y1 = self.y + 350
        self.canvas.delete(self.tag)
        self.canvas.create_rectangle(x0,y0,x1,y1,tags=self.tag, fill=self.color)

'''
Défini la barre se trouvant au milieu du terrain séparant les 2 joueurs. Elle est dessinée à l'initialisation du jeu,
avec redraw lancé à la fin de l'initialisation.
'''

class Bord:
    def __init__(self, canvas, tag, color="green", x=0, y=0): #défini les attribus des bords du terrain à l'initialisation du jeu
        self.canvas = canvas
        self.tag = tag
        self.x = x
        self.y = y
        self.color = color
        self.redraw()

    def redraw(self): #Dessine les bords
        x0 = self.x - 1000
        x1 = self.x + 1000
        y0 = self.y - 20
        y1 = self.y 
        self.canvas.delete(self.tag)
        self.canvas.create_rectangle(x0,y0,x1,y1,tags=self.tag, fill=self.color)

'''
Défini les bords du terrain. Ils sont d'abord initialisés, et dessinés à l'initialisation du jeu en haut et en bas du 
terrain avec redraw. La balle rebondit sur eux.
'''

        
       


