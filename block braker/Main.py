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
angulo = -90


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


def mostrarMensaje(mensaje):
    fuente = pygame.font.Font(None, 100)
    texto = fuente.render(mensaje, True, getColor("BLANCO"))
    rectangulo_texto = texto.get_rect(center=(ANCHO//2, ALTO -80))
    VENTANA.blit(texto, rectangulo_texto)



def colisiones(pelota_objeto, pelota, bloques_objetos, pos, ancho_bloque, alto_bloque):
    for i in range(len(pos)):
        for j in range(len(pos[i])):
            horizontal = [pos[i][0][0], pos[i][0][0]+ancho_bloque]
            vertical = [pos[i][0][1], pos[i][0][1]+alto_bloque]


        for x in range(horizontal[0], horizontal[1]):
            for y in range(horizontal[0], horizontal[1]):
                if pelota_objeto.collidepoint(x, y):
                    Pelota.setVelocidad(pelota, 0)



plataforma = Plataforma.constructor(color=getColor("AZUL"),
                                    ancho=80,
                                    alto=20,
                                    x=400,
                                    y=570,
                                    velocidad=10)
pelota = Pelota.constructor(color=getColor("SALMON"),
                            x=ANCHO//2,
                            y=500,
                            velocidad=2.5,
                            radio=20)




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

    # Dibujamos todos los objetos
    plataforma_objeto  = pygame.draw.rect(VENTANA,
                        Plataforma.getColor(plataforma),
                        (Plataforma.getX(plataforma),
                        Plataforma.getY(plataforma),
                        Plataforma.getAncho(plataforma),
                        Plataforma.getAlto(plataforma)))
    pelota_objeto = pygame.draw.circle(VENTANA, (215, 97, 49), (Pelota.getX(pelota), Pelota.getY(pelota)), Pelota.getRadio(pelota))

    bloques_objetos = list()
    boredes_objetos = list()
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

        colisiones(centro_bloque=(Bloque.getX(bloque), Bloque.getY(bloque)))



    # Calculamos la nueva posicion de pelota
    x, y = movimientoPelota(angulo, Pelota.getVelocidad(pelota))
    Pelota.setX(pelota, x + Pelota.getX(pelota))
    Pelota.setY(pelota, y + Pelota.getY(pelota))


    # Actualizamos la posicion de la plataforma segun el input
    boton = pygame.key.get_pressed()
    movimientoPlataforma(boton)


    # Calculamos colisiones
    colisiones(pelota_objeto, pelota, bloques_objetos, pos, ancho_bloque, alto_bloque)

    # Refrescamos la pantalla
    pygame.display.update()

    # Bucle final de eventos
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            run = False
            pygame.quit()
