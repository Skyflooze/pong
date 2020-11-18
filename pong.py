#pong


from tkinter import *

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

dx = 5
dy = 5

def balle_move():
    global dx, dy
    
    if (canvas.coords(balle1)[3]>292) or (canvas.coords(balle1)[1]<0):
        dy=-1*dy
    if (canvas.coords(balle1)[0]<0) or (canvas.coords(balle1)[2]>500):
        dx=-1*dx
    
    canvas.move(balle1,dx,dy)
    root.after(20,balle_move)



root = Tk()
canvas = Canvas(root, width=largeur, height=hauteur, background="black")


raquette1_canvas = canvas.create_rectangle(6, 125,  11, 175, width=1, fill="white", outline="")
raquette2_canvas = canvas.create_rectangle(497, 125, 492, 175, width=1, fill="white", outline="")
balle1 = canvas.create_oval(240,120,260,140,fill='red')
bord_haut = canvas.create_rectangle(0, 0, 503, 10, fill='green')
bord_bas = canvas.create_rectangle(0, 292, 503, 302, fill='green')


canvas.bind_all('<z>', raquette1_haut)
canvas.bind_all('<s>', raquette1_bas)
canvas.bind_all('<o>', raquette2_haut)
canvas.bind_all('<l>', raquette2_bas)

v = StringVar()
v.set("")
canvas.pack()
Label(root, textvariable=v).pack()
v.set("")
balle_move()
root.mainloop()
