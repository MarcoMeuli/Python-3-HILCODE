import pygame
from colores import *

ANCHO= 300
ALTO= 400
run= True

VENTANA= pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tic Tac Toe")

def dibujarX():
    pygame.draw.line(surface=VENTANA, width=5, color=getColor("BLANCO"), start_pos=(0,0), end_pos=(100,100))
    pygame.draw.line(surface=VENTANA, width=5, color=getColor("BLANCO"), start_pos=(100,0), end_pos=(0,100))

def dibujarO():
    pygame.draw.circle(VENTANA, getColor("BLANCO"), (50, 50), 40)

VENTANA.fill(getColor("NEGRO"))
pygame.draw.line(surface=VENTANA,width=3,color=getColor("ROJO"),start_pos=(0, 100),end_pos=(ANCHO, 100))
pygame.draw.line(surface=VENTANA,width=3,color=getColor("ROJO"),start_pos=(0, 200),end_pos=(ANCHO, 200))
pygame.draw.line(surface=VENTANA,width=3,color=getColor("ROJO"),start_pos=(0, 300),end_pos=(ANCHO, 300))
pygame.draw.line(surface=VENTANA,width=3,color=getColor("ROJO"),start_pos=(100, 0),end_pos=(100, 300))
pygame.draw.line(surface=VENTANA,width=3,color=getColor("ROJO"),start_pos=(200, 0),end_pos=(200, 300))
dibujarO()




pygame.display.update()
