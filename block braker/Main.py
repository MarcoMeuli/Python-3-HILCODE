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
    rad = (math.pi*angulo)/180
    x = math.cos(rad)*vel
    y = math.sin(rad)*vel
    return x, y


def movimientoPlataforma(boton):
    if boton[pygame.K_LEFT] or boton[pygame.K_a]:
        nueva_x = Plataforma.getX(plataforma) - Plataforma.getVelocidad(plataforma)
        if nueva_x >= 0:
            Plataforma.setX(plataforma, nueva_x)
    if boton[pygame.K_RIGHT] or boton[pygame.K_d]:
        nueva_x = Plataforma.getX(plataforma) + Plataforma.getVelocidad(plataforma)
        if nueva_x + Plataforma.getAncho(plataforma) <= ANCHO:
            Plataforma.setX(plataforma, nueva_x)


plataforma = Plataforma.constructor(color=getColor("AZUL"),
                                    ancho=80,
                                    alto=20,
                                    x=400,
                                    y=570,
                                    velocidad=10)
pelota = Pelota.constructor(color=getColor("SALMON"),
                            x=400,
                            y=300,
                            velocidad=2.5,
                            radio=15)

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



run = True
while run:
    VENTANA.fill(getColor("NEGRO"))

                        ##PRINTS##
    pygame.draw.rect(VENTANA,
            Plataforma.getColor(plataforma),
            (Plataforma.getX(plataforma),
            Plataforma.getY(plataforma),
            Plataforma.getAncho(plataforma),
            Plataforma.getAlto(plataforma)))


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
                        ##PRINTS##

    x, y = movimientoPelota(angulo, Pelota.getVelocidad(pelota))
    Pelota.setX(pelota, x + Pelota.getX(pelota))
    Pelota.setY(pelota, y + Pelota.getY(pelota))

    pygame.draw.circle(VENTANA, (215, 97, 49), (Pelota.getX(pelota), Pelota.getY(pelota)), Pelota.getRadio(pelota))

    boton = pygame.key.get_pressed()
    movimientoPlataforma(boton)


    pygame.display.update()
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            run = False
            pygame.quit()
