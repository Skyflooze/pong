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

def deplacement():
    global dx, dy
    if (canvas.coords(balle1)[3]>300) or (canvas.coords(balle1)[1]<0):
        dy=-1*dy
    if (canvas.coords(balle1)[0]<0) or (canvas.coords(balle1)[2]>500):
        dx=-1*dx
        

    #Test de la collision avec la raquette par coordonnees:
    if (canvas.coords(balle1)[3]>canvas.coords(raquette1_canvas)[1]) and (canvas.coords(balle1)[0]<canvas.coords(raquette1_canvas)[2]) and (canvas.coords(balle1)[2]>canvas.coords(raquette1_canvas)[0]):
        dy=-1*dy
   
    #On deplace la balle :
    canvas.move(balle1,dx,dy)
   
    #On repete cette fonction
    root.after(20,deplacement)

          

root = Tk()
canvas = Canvas(root, width=largeur, height=hauteur, background="black")


x_raq1, y_raq1 = 3,125
dx=5
dy=5

raquette1_canvas = canvas.create_rectangle(3, 125,  8, 175, width=1, fill="white", outline="")
raquette2_canvas = canvas.create_rectangle(497, 125, 492, 175, width=1, fill="white", outline="")
balle1 = canvas.create_oval(240,120,260,140,fill='red')
raquette = Raquettes(0)

canvas.bind_all('<z>', raquette1_haut)
canvas.bind_all('<s>', raquette1_bas)
canvas.bind_all('<o>', raquette2_haut)
canvas.bind_all('<l>', raquette2_bas)

v = StringVar()
v.set("wesh")
canvas.pack()
Label(root, textvariable=v).pack()
v.set("")
deplacement()
root.mainloop()
