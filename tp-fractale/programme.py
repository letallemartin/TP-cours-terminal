from turtle import *
# speed(10)
# forward(100)
# left(30)
# forward(80)

def arbre_fractale2(L):

    forward(L)
    
    left(30)
    forward(L*0.8)
    backward(L*0.8)
    
    right(60)
    forward(L*0.8)
    backward(L*0.8)
    left(30)
    backward(L)


    
def arbre_fractal3(L, n):
    forward(L)

    # Branche gauche (arbre de profondeur 2)
    left(30)
    arbre_fractale2(0.8 * L)
    right(30)

    # Branche droite (arbre de profondeur 2)
    right(30)
    arbre_fractale2(0.8 * L)
    left(30)

    # Retour au point de départ (maintien de la position initiale)
    backward(L)
    
    
        
def arbre(L, n, R, ang1, ang2):
    if n == 0:
        return 0
    pensize(L / 15)  # Trait de 5 pixels d'épaisseur (ou width(5))
    forward(L)
    
    left(ang1)
    arbre(L * R, n - 1, R, ang1, ang2)
    
    right(ang2)
    
    arbre(L * R, n - 1, R, ang1, ang2)
    left(ang1)
    
    backward(L)

penup()
goto(0, -250)
pendown()
left(90)
speed(10000000)
arbre(100,  7, 0.6, 30, 60)
done()
