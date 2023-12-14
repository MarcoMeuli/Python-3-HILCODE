import planets_utils
import pygame
import math

ANCHO = 1080
ALTO = 720
CENTRO = (ANCHO/2, ALTO/2)
NOMBRE = "sistema solar"

VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(NOMBRE)

def movimiento(radio, centro_x, centro_y, angulo):
    x = centro_x + int(math.cos(angulo)*radio)
    y = centro_y + int(math.sin(angulo)*radio)
    return x, y


sol = planets_utils.constructorPlanetas(nombre="sol", tam=35, x=CENTRO[0], y=CENTRO[1], radio=0, color=(255,255,0))
mercurio = planets_utils.constructorPlanetas(nombre="mercurio", tam=3, radio=50, color=(162,162,162))
venus = planets_utils.constructorPlanetas(nombre="venus", tam=6, radio=100, color=(228,163,98))
tierra = planets_utils.constructorPlanetas(nombre="tierra", tam=10, radio=150, color=(28,156,0))
marte = planets_utils.constructorPlanetas(nombre="marte", tam=12, radio=200, color=(252,34,0))
jupiter = planets_utils.constructorPlanetas(nombre="jupiter", tam=23, radio=250, color=(131,48,21))
saturno = planets_utils.constructorPlanetas(nombre="saturno", tam=18, radio=300, color=(252,200,0))
urano = planets_utils.constructorPlanetas(nombre="urano", tam=15, radio=350, color=(107,217,255))
neptuno = planets_utils.constructorPlanetas(nombre="neptuno", tam=8, radio=400, color=(0,100,255))


pygame.draw.circle(VENTANA,
planets_utils.getColor(sol),
(planets_utils.getX(sol),
planets_utils.getY(sol)),
planets_utils.getTam(sol))


pygame.draw.circle(VENTANA,
planets_utils.getColor(mercurio),
(planets_utils.getX(mercurio),
planets_utils.getY(mercurio)),
planets_utils.getTam(mercurio))

pygame.display.update()
