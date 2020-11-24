#pong

from tkinter import *
from pong_class import *

largeur = 500
hauteur = 300


def raquette1_haut(event):
    canvas.move(raquette1_canvas,0,-5)

def raquette1_bas(event):
    canvas.move(raquette1_canvas,0,5)

def raquette2_haut(event):
    canvas.move(raquette2_canvas,0,-5)

def raquette2_bas(event):
    canvas.move(raquette2_canvas,0,5)


def balle_move():
    score_j1 = 0
    score_j2 = 0
    if (canvas.coords(balle1)[3]>292) or (canvas.coords(balle1)[1]<10):
        mouv.by=-1*mouv.by
    if (canvas.coords(balle1)[3]>canvas.coords(raquette1_canvas)[1]) and (canvas.coords(balle1)[0]<canvas.coords(raquette1_canvas)[2]) and (canvas.coords(balle1)[2]>canvas.coords(raquette1_canvas)[0]):
        mouv.bx=-1*mouv.bx
    if (canvas.coords(balle1)[3]>canvas.coords(raquette2_canvas)[1]) and (canvas.coords(balle1)[0]<canvas.coords(raquette2_canvas)[2]) and (canvas.coords(balle1)[2]>canvas.coords(raquette2_canvas)[0]):
        mouv.bx=-1*mouv.bx
    if (canvas.coords(balle1)[0]<0):
        canvas.delete(ALL)
        text.insert(INSERT, "GAME OVER\n")
        text.pack()
        score_j1 += 1
        text.insert(INSERT, f"Score du joueur 2 : {score_j1}")
    if (canvas.coords(balle1)[2]>500):
        text.insert(INSERT, "GAME OVER\n")
        text.pack()
        canvas.delete(ALL)
        score_j2 += 1
        text.insert(INSERT, f"Score du joueur 1 : {score_j2}")
    

    canvas.move(balle1,mouv.bx,mouv.by)
    root.after(20,balle_move)



root = Tk()
text = Text(root)
mouv = Raquettes()

canvas = Canvas(root, width=largeur, height=hauteur, background="black")
raquette1_canvas = canvas.create_rectangle(6, 125,  11, 175, width=1, fill="white", outline="")
raquette2_canvas = canvas.create_rectangle(497, 125, 492, 175, width=1, fill="white", outline="")
balle1 = canvas.create_oval(240,120,260,140,fill='red')
bord_haut = canvas.create_rectangle(0, 0, 503, 10, fill='green')
bord_bas = canvas.create_rectangle(0, 292, 503, 302, fill='green')

root.bind('<z>', raquette1_haut)
root.bind('<s>', raquette1_bas)
root.bind('<o>', raquette2_haut)
root.bind('<l>', raquette2_bas)

v = StringVar()

label_score = Label(root, text = "score")
label_score.pack()
canvas.pack()
Label(root, textvariable=v).pack()
balle_move()
root.mainloop()
