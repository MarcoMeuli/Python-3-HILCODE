# MAIN

import Bloque
import Pelota
import Plataforma
import random
import pygame
import math
from colores import *
from Mapas_utils import pos
from Mapas import mapa1
pygame.init()



ANCHO, ALTO = 800, 600
pygame.display.set_caption("Block Breaker")
VENTANA = pygame.display.set_mode((ANCHO, ALTO))


angulo = random.randint(0, 360)
def movimientoPelota(angulo, vel):
    i = (math.pi*angulo)/180
    x = math.cos(i)*vel
    y = math.sin(i)*vel
    return x, y


plataforma = Plataforma.constructor(color=getColor("AZUL"), ancho=80, alto=20, x=400, y=570, velocidad=7)
pelota = Pelota.constructor(color=getColor("SALMON"), x=400, y=300, velocidad=0.5,radio=20)

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



run=True
while run == True:
    VENTANA.fill(getColor("NEGRO"))

                        ##-##
    pygame.draw.rect(
            VENTANA,
            Plataforma.getColor(plataforma),
            (Plataforma.getX(plataforma),
            Plataforma.getY(plataforma),
            Plataforma.getAncho(plataforma),
            Plataforma.getAlto(plataforma)))
                        ##-##




                        ##-##
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
                        ##-##





    x, y = movimientoPelota(angulo, Pelota.getVelocidad(pelota))
    Pelota.setX(pelota, x + Pelota.getX(pelota))
    Pelota.setY(pelota, y + Pelota.getY(pelota))

    pygame.draw.circle(VENTANA, (215, 97, 49), (Pelota.getX(pelota), Pelota.getY(pelota)), Pelota.getRadio(pelota))

    pygame.display.update()

    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            ejecutar = False


