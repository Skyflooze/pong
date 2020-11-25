#pong
from tkinter import *
from pong_class import *

largeur = 500
hauteur = 300

def raquette1_haut(event):
    if (canvas.coords(raquette1_canvas)[1]<=0):
        canvas.move(raquette1_canvas,0,0)
    else:
        canvas.move(raquette1_canvas,0,-5)

def raquette1_bas(event):
    if (canvas.coords(raquette1_canvas)[1]>=220):
        canvas.move(raquette1_canvas,0,0)
    else:
        canvas.move(raquette1_canvas,0,5)

def raquette2_haut(event):
    if (canvas.coords(raquette2_canvas)[1]<=0):
        canvas.move(raquette2_canvas,0,0)
    else:
        canvas.move(raquette2_canvas,0,-5)

def raquette2_bas(event):
    if (canvas.coords(raquette2_canvas)[1]>=220):
        canvas.move(raquette2_canvas,0,0)
    else:
        canvas.move(raquette2_canvas,0,5)


def balle_move():
    if (canvas.coords(balle1)[3]>292) or (canvas.coords(balle1)[1]<10):
        raq.by=-1*raq.by
    if (canvas.coords(balle1)[3]>canvas.coords(raquette1_canvas)[1]) and (canvas.coords(balle1)[0]<canvas.coords(raquette1_canvas)[2]) and (canvas.coords(balle1)[2]>canvas.coords(raquette1_canvas)[0]):
        raq.bx=-1*raq.bx
        raq.bx = raq.bx*1.1
    if (canvas.coords(balle1)[3]>canvas.coords(raquette2_canvas)[1]) and (canvas.coords(balle1)[0]<canvas.coords(raquette2_canvas)[2]) and (canvas.coords(balle1)[2]>canvas.coords(raquette2_canvas)[0]):
        raq.bx=-1*raq.bx
        raq.bx = raq.bx*1.1
    if (canvas.coords(balle1)[0]<0):
        raq.scorej1 += 1
        est_mort()
    if (canvas.coords(balle1)[2]>500):
        raq.scorej2 += 1
        est_mort()

    canvas.move(balle1,raq.bx,raq.by)
    root.after(20,balle_move)


def est_mort():
    canvas.delete(ALL)
    text.insert(INSERT, "GAME OVER\n")
    text.pack()
    text.insert(INSERT, f"Score du joueur 1 : {raq.scorej1}\nScore du joueur 2 : {raq.scorej2}")
    
root = Tk()
text = Text(root)
raq = Raquettes()

canvas = Canvas(root, width=largeur, height=hauteur, background="black")
raquette1_canvas = canvas.create_rectangle(6, 125,  11, 200, width=1, fill="white", outline="")
raquette2_canvas = canvas.create_rectangle(497, 125, 492, 200, width=1, fill="white", outline="")
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
