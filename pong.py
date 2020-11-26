#pong

from tkinter import *
from pong_class import * #importe le contenu de pong_class.py où se situe les classes

def balle_move():
    if (jeu.canvas.coords(jeu.balle)[3]>292) or (jeu.canvas.coords(jeu.balle)[1]<10):
        jeu.balle.by=-1*jeu.balle.by
    if (jeu.canvas.coords(jeu.balle)[3]>jeu.canvas.coords(raquette1)[1]) and (jeu.canvas.coords(jeu.balle)[0]<jeu.canvas.coords(raquette1)[2]) and (jeu.canvas.coords(jeu.balle)[2]>jeu.canvas.coords(raquette1)[0]):
        jeu.balle.bx=-1*jeu.balle.bx
    if (jeu.canvas.coords(jeu.balle)[3]>jeu.canvas.coords(raquette2)[1]) and (jeu.canvas.coords(jeu.balle)[0]<jeu.canvas.coords(raquette2)[2]) and (jeu.canvas.coords(jeu.balle)[2]>jeu.canvas.coords(raquette2)[0]):
        jeu.balle.bx=-1*jeu.balle.bx
    if (jeu.canvas.coords(jeu.balle)[0]<0):
        jeu.jeu.canvas.delete(ALL)
    if (jeu.canvas.coords(jeu.balle)[2]>500):
        jeu.canvas.delete(ALL)
        
    jeu.canvas.move(jeu.balle,jeu.balle.bx,jeu.balle.by)
    root.after(20,jeu.balle_move)

'''
Les mouvements de la balle. Elle se déplace avec les coordonnées de x et y de manière constante, et rebondi 
sur les raquettes lorsqu'elle elles les touches pour repartir dans l'axe x contraire. Lorsqu'elle passe un certain
seuil, à droite ou à gauche, quand elle est derrière les raquettes, alors la manche s'arrête.
'''


jeu = Game() #défini la classe Game de pong_class comme jeu afin d'être appelée dans balle_move
jeu.start() #lance le jeu
balle_move() #appelle la fonction balle_move
