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
    posiciones=[[   [50,50],
                    [150,50],
                    [250,50]    ],

                [   [50,150],
                    [150,150],
                    [250,150]   ],

                [   [50,250],
                    [150,250],
                    [250,250]   ]]

    resultado=posiciones[0][0] if pos == 1
    resultado=posiciones[0][1] elif pos == 2
    resultado=posiciones[0][2] elif pos == 3
    resultado=posiciones[1][0] elif pos == 4
    resultado=posiciones[1][1] elif pos == 5
    resultado=posiciones[1][2] elif pos == 6
    resultado=posiciones[2][0] elif pos == 7
    resultado=posiciones[2][1] elif pos == 8
    resultado=posiciones[2][2] elif pos == 9

    return resultado



def posX():
    posiciones=[[   [[(0,0),(100,100)],[(0,100),(100,0)]],
                    [[(100,0),(200,100)],[(100,100),(200,0)]],
                    [[(200,0),(300,100)],[(200,100),(300,0)]]   ],

                [   [[(0,100),(100,200)],[(0,200),(100,100)]],
                    [[(100,100),(200,200)],[(100,200),(200,100)]],
                    [[(200,100),(300,200)],[(200,200),(300,100)]]   ],

                [   [[(0,200),(100,300)],[(0,300),(100,200)]],
                    [[(100,200),(200,300)],[(100,300),(200,200)]],
                    [[(200,200),(300,300)],[(200,300),(300,200)]]   ]]
    return posiciones



VENTANA.fill(getColor("NEGRO"))
dibujarTabla()
posO(1)

pygame.display.update()
