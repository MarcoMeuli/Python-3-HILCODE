import planets_utils
import pygame
import math

ANCHO = 1600
ALTO = 900
CENTRO = (ANCHO/2, ALTO/2)
NOMBRE = "sistema solar"

VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(NOMBRE)

def movimiento(radio, centro_x, centro_y, angulo):
    x = centro_x + int(math.cos(angulo)*radio)
    y = centro_y + int(math.sin(angulo)*radio)
    return x, y

mercurio = planets_utils.constructorPlanetas(nombre="mercurio", tam=3, radio=50, color=(162,162,162))
