from turtle import*
import random
def segment(long):
    forward(long)
    left(60)
    forward(long)
    right(120)
    forward(long)
    left(60)

def segmentR(long,n):
    liste = ["red", "blue", "green","purple"]
    x = random.randint(0,3)
    pencolor(liste[x])
    if n == 0:   
        forward(long)
    if n > 0:
        segmentR(long/ 3,n - 1)
        left(60)
        segmentR(long/ 3,n - 1)
        right(120) 
        segmentR(long/ 3,n - 1)
        left(60)
        segmentR(long/ 3,n - 1)

def flocon(long, n):
    pensize(2)
    for i in range(3):
        segmentR(long,n)
        right(120)
        
    
    
speed(0)
flocon(200, 3)

done()