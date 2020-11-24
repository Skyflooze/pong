#pong


from tkinter import *

largeur = 500
hauteur = 300


#mouvement des raquettes
def raquette1_haut(event):
    canvas.move(raquette1_canvas,0,-5)

def raquette1_bas(event):
    canvas.move(raquette1_canvas,0,5)

def raquette2_haut(event):
    canvas.move(raquette2_canvas,0,-5)

def raquette2_bas(event):
    canvas.move(raquette2_canvas,0,5)

#vitesse de la balle en x et y
bx = 4
by = 4

#mouvement de la balle
def balle_move():
    global bx, by
    score_j1 = 0
    score_j2 = 0
    if (canvas.coords(balle1)[3]>292) or (canvas.coords(balle1)[1]<10):  #collision avec les bordures
        by=-1*by
    if (canvas.coords(balle1)[3]>canvas.coords(raquette1_canvas)[1]) and (canvas.coords(balle1)[0]<canvas.coords(raquette1_canvas)[2]) and (canvas.coords(balle1)[2]>canvas.coords(raquette1_canvas)[0]):  #collision avec raquette 1
        bx=-1*bx
    if (canvas.coords(balle1)[3]>canvas.coords(raquette2_canvas)[1]) and (canvas.coords(balle1)[0]<canvas.coords(raquette2_canvas)[2]) and (canvas.coords(balle1)[2]>canvas.coords(raquette2_canvas)[0]):  #collision avec raquette 2
        bx=-1*bx
    if (canvas.coords(balle1)[0]<0):  #augmentation du score_j1
        score_j1 += 1
        v.set(f"Score du joueur 2 : {score_j1}")
    if (canvas.coords(balle1)[2]>500):  #augmentation du score_j2
        score_j2 += 1
        v.set(f"Score du joueur 1 : {score_j2}")


    
    canvas.move(balle1,bx,by)
    root.after(20,balle_move)



root = Tk()
canvas = Canvas(root, width=largeur, height=hauteur, background="black")  #creation de la fenetre

#créations des canvas
raquette1_canvas = canvas.create_rectangle(6, 125,  11, 175, width=1, fill="white", outline="")
raquette2_canvas = canvas.create_rectangle(497, 125, 492, 175, width=1, fill="white", outline="")
balle1 = canvas.create_oval(240,120,260,140,fill='red')
bord_haut = canvas.create_rectangle(0, 0, 503, 10, fill='green')
bord_bas = canvas.create_rectangle(0, 292, 503, 302, fill='green')

#touches pour les raquettes
canvas.bind_all('<z>', raquette1_haut)
canvas.bind_all('<s>', raquette1_bas)
canvas.bind_all('<o>', raquette2_haut)
canvas.bind_all('<l>', raquette2_bas)

v = StringVar()

label_score = Label(root, text = "score")
label_score.pack()
canvas.pack()
Label(root, textvariable=v).pack()
balle_move()  #appel de la fonction balle move
root.mainloop()
