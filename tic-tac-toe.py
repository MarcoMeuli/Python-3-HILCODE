import pygame
from colores import *

ANCHO= 300
ALTO= 400
run= True
VENTANA= pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tic Tac Toe")

def dibujarTabla():
    pygame.draw.line(surface=VENTANA,width=3,color=getColor("ROJO"),start_pos=(0, 100),end_pos=(ANCHO, 100))
    pygame.draw.line(surface=VENTANA,width=3,color=getColor("ROJO"),start_pos=(0, 200),end_pos=(ANCHO, 200))
    pygame.draw.line(surface=VENTANA,width=3,color=getColor("ROJO"),start_pos=(0, 300),end_pos=(ANCHO, 300))
    pygame.draw.line(surface=VENTANA,width=3,color=getColor("ROJO"),start_pos=(100, 0),end_pos=(100, 300))
    pygame.draw.line(surface=VENTANA,width=3,color=getColor("ROJO"),start_pos=(200, 0),end_pos=(200, 300))

def dibujarX():
    pygame.draw.line(surface=VENTANA, width=5, color=getColor("BLANCO"), start_pos=(0,0), end_pos=(100,100))
    pygame.draw.line(surface=VENTANA, width=5, color=getColor("BLANCO"), start_pos=(0,100), end_pos=(100,0))

def dibujarO():
    pygame.draw.circle(VENTANA, getColor("BLANCO"), (50, 50), 40)

def posO(pos):
    posiciones=[[   [1,2,3],
                    [4,5,6],
                    [7,8,9] ]

                [   [50,150,250],
                    [50,150,250],
                    [50,150,250] ]

                [   [50,50,50],
                    [150,150,150],
                    [250,250,250] ]]


def posX():
    posiciones={    1: ([(0,0),(100,100)], [(0,100),(100,0)]),
                    2: ([(100,0),(200,100)], [(0,100),(100,0)]),
                    3: ([(200,0),(300,100)], [(200,100),(300,0)]),
                    4: ([(200,0),(300,100)], [(200,100),(300,0)]),
                    5: ([(100,100),(200,200)], [(100,200),(200,100)])   }




VENTANA.fill(getColor("NEGRO"))
dibujarTabla()
posO()

pygame.display.update()
