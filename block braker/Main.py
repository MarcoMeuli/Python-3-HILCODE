# MAIN

import Bloque
import Pelota
import Plataforma
import random
import pygame
import math
from colores import *
from Mapas_utils import *
from Mapas import mapa1
pygame.init()



ANCHO, ALTO = 800, 600
pygame.display.set_caption("Block Breaker")
VENTANA = pygame.display.set_mode((ANCHO, ALTO))

angulo = -90
ancho_bloque = 40
alto_bloque = 20
num_filas = 10

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
            horizontal = [pos[i][j][0], pos[i][j][0]+ancho_bloque]
            vertical = [pos[i][j][1], pos[i][j][1]+alto_bloque]

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
                            velocidad=10,
                            radio=20)


pos = generar_pos(ancho_bloque = ancho_bloque,
                  ancho_pantalla = 800,
                  alto_bloque = alto_bloque,
                  num_filas = num_filas)

mapa = generar_map(ancho_bloque = ancho_bloque,
                   ancho_pantalla = 800,
                   alto_bloque = alto_bloque,
                   num_filas = num_filas)


bloques = list()
bloques_objetos = list()
borde_objetos = list()
for i in range(len(mapa1)):
    for j in range(len(mapa1[i])):
        if mapa1[i][j]:
            bloque = Bloque.constructor(color = getColor("AMARILLO"),
                                         ancho = ancho_bloque,
                                         alto = alto_bloque,
                                         x = pos[i][j][0],
                                         y = pos[i][j][1],
                                         estado = 3)
            bloques.append(bloque)


run = True
while run:

    # Bucle de eventos
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            run = False

    # Dibujamos el fondo
    VENTANA.fill(getColor("NEGRO"))

    # Dibujamos la plataforma
    plataforma_objeto  = pygame.draw.rect(VENTANA,
                        Plataforma.getColor(plataforma),
                        (Plataforma.getX(plataforma),
                        Plataforma.getY(plataforma),
                        Plataforma.getAncho(plataforma),
                        Plataforma.getAlto(plataforma)))

    # Dibujamos la pelota
    pelota_objeto = pygame.draw.circle(VENTANA,
                                      (215, 97, 49),
                                      (Pelota.getX(pelota),
                                      Pelota.getY(pelota)),
                                      Pelota.getRadio(pelota))

    #Dibujamos los bloques
    bloques_objetos = list()
    bordes_objetos = list()
    for bloque in bloques:
        bloque_objeto = pygame.draw.rect(
                            VENTANA,
                            Bloque.getColor(bloque),
                            (Bloque.getX(bloque),
                            Bloque.getY(bloque),
                            Bloque.getAncho(bloque),
                            Bloque.getAlto(bloque)))

        bloques_objetos.append(bloque_objeto)

        borde_objeto = pygame.draw.rect(
                surface = VENTANA,
                color = getColor("NEGRO"),
                width = 1,
                rect = (Bloque.getX(bloque),
                Bloque.getY(bloque),
                Bloque.getAncho(bloque),
                Bloque.getAlto(bloque)))

        bordes_objetos.append(borde_objeto)




    # Calculamos la nueva posicion de pelota
    x, y = movimientoPelota(angulo, Pelota.getVelocidad(pelota))
    Pelota.setX(pelota, x + Pelota.getX(pelota))
    Pelota.setY(pelota, y + Pelota.getY(pelota))


    # Actualizamos la posicion de la plataforma segun el input
    boton = pygame.key.get_pressed()
    movimientoPlataforma(boton)


    # Calculamos colisiones de los bloques
    colisiones(pelota_objeto, pelota, bloques_objetos, pos, ancho_bloque, alto_bloque)

    # Refrescamos la pantalla
    pygame.display.update()
pygame.quit()
