# import tkinter as tk
# fenetre = tk.Tk()
# fenetre.title("Zone de dessin")
# canevas = tk.Canvas(
# fenetre,
# width=600,
# height=400,
# bg="lightblue"
# )
# canevas.pack()
# fenetre.mainloop()

# import tkinter as tk
# fenetre = tk.Tk()
# fenetre.title("Premiers dessins")
# canevas = tk.Canvas(
# fenetre, width=600, height=400, bg="white")
# canevas.pack()

# canevas.create_rectangle(
# 50, 50, 200, 250, fill="lightblue")
# canevas.create_oval(
# 0, 50, 100, 150, fill="tomato")
# canevas.create_line(
# 50, 250, 350, 300, width=4, fill="green")
# fenetre.mainloop()

import tkinter as tk
# fenetre = tk.Tk()
# fenetre.title("Modifier un dessin")
# canevas = tk.Canvas(
# fenetre, width=600, height=400, bg="white"
# )
# canevas.pack()
# balle = canevas.create_oval(
# 40, 40, 80, 80, fill="blue"
# )
# canevas.coords(balle, 200, 150, 240, 190)
# print(balle)
# fenetre.mainloop()

# def changer_couleur():
#     canevas.itemconfig(balle, fill="blue")

# def changer_couleur2():
#     canevas.itemconfig(balle, fill="yellow")
    
# fenetre = tk.Tk()
# fenetre.title("Fenêtre avec un bouton")
# canevas = tk.Canvas(
# fenetre, width=400, height=250, bg="white"
# )
# canevas.pack()
# balle = canevas.create_oval(
# 150, 80, 200, 130, fill="red"
# )
# bouton = tk.Button(
# fenetre,
# text="Changer la couleur",
# command=changer_couleur
# )

# bouton2 = tk.Button(
# fenetre,
# text="Changer la couleur 2 ",
# command=changer_couleur2
# )
# bouton2.pack()
# bouton.pack()
# fenetre.mainloop()
import tkinter as tk

def deplacer():
    canevas.move(balle, 3, 0) # Déplace la balle de 3 pixels vers la droite sur le canevas
    fenetre.after(30, deplacer) # Délai de 30ms avant l’appel de la fonction deplacer

def arreter():
    fenetre.after_cancel(animation)

def augmenter():
    global vx, vy
    if vx > 0:
        vx += 1
    else:
        vx -= 1
    if vy > 0:
        vy += 1
    else:
        vy -= 1

def diminuer():
    global vx, vy
    if vx > 0:
        vx -= 1
    else:
        vx += 1
    if vy > 0:
        vy -= 1
    else:
        vy += 1
    
    
    
def animer():
    global x, y, vx, vy, animation
    x = x + vx
    y = y + vy
    # canevas.coords() met à jour la position du dessin à l'écran.
    
    animation = fenetre.after(30, animer)
    if x <= rayon or x >= largeur - rayon:
        vx = -vx
    if y <= rayon or y >= hauteur - rayon:
        vy = -vy
    
    canevas.coords(
        balle,
        x - rayon, y - rayon,
        x + rayon, y + rayon
        )



fenetre = tk.Tk()
fenetre.title("Déplacer une balle")
largeur = 600
hauteur = 400
rayon = 20
x = 60
y = 60
vx = 3
vy = 2

canevas = tk.Canvas(
fenetre,
width=600,
height=400,
bg="white")
canevas.pack()
balle = canevas.create_oval(
x - rayon, y - rayon,
x + rayon, y + rayon,
fill="blue"
)
bouton = tk.Button(
fenetre,
text="Déplacer",
command=animer
)
bouton2 = tk.Button(
fenetre,
text="arreter",
command=arreter
)
bouton3 = tk.Button(
fenetre,
text="augmenter",
command=augmenter
)

bouton4 = tk.Button(
fenetre,
text="diminuer",
command=diminuer
)
#fenetre.after(100, animer)
bouton.pack()
bouton3.pack()
bouton2.pack()
bouton4.pack()
fenetre.mainloop()