# MAIN

import Bloque
import Pelota
import Plataforma
import random
import pygame
from colores import *
from Mapas_utils import pos
from Mapas import mapa1
pygame.init()



ANCHO, ALTO = 800, 600
pygame.display.set_caption("Block Breaker")
VENTANA = pygame.display.set_mode((ANCHO, ALTO))

plataforma = Plataforma.constructor(color=getColor("AZUL"), ancho=80, alto=20, x=400, y=570, velocidad=7)
pelota = Pelota.constructor(color=getColor("SALMON"), x=400, y=300, velocidad=7,radio=20)



# Dibujo el fondo y la pelota
VENTANA.fill(getColor("NEGRO"))
pygame.draw.rect(
            VENTANA,
            Plataforma.getColor(plataforma),
            (Plataforma.getX(plataforma),
            Plataforma.getY(plataforma),
            Plataforma.getAncho(plataforma),
            Plataforma.getAlto(plataforma)))

pygame.draw.circle(
            VENTANA,
            Pelota.getColor(pelota),
            (Pelota.getX(pelota),
            Pelota.getY(pelota)),
            Pelota.getRadio(pelota))



bloques = list()
for i in range(len(mapa1)):
    for j in range(len(mapa1[i])):
        if mapa1[i][j]:
            bloque = Bloque.constructor(color = getColor("AMARILLO"),
                                         ancho = 40,
                                         alto = 20,
                                         x = pos[i][j][0],
                                         y = pos[i][j][1],
                                         estado = 3)
            bloques.append(bloque)

for bloque in bloques:
    pygame.draw.rect(
            VENTANA,
            Bloque.getColor(bloque),
            (Bloque.getX(bloque),
            Bloque.getY(bloque),
            Bloque.getAncho(bloque),
            Bloque.getAlto(bloque)))

    pygame.draw.rect(
            surface = VENTANA,
            color = getColor("NEGRO"),
            width = 1,
            rect = (Bloque.getX(bloque),
            Bloque.getY(bloque),
            Bloque.getAncho(bloque),
            Bloque.getAlto(bloque)))

pygame.display.update()
