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


x_tierra = CENTRO[0]+400
y_tierra = CENTRO[1]
angulo_tierra = 0
velocidad_angular = 0.01




ejecutar = True
while ejecutar == True:
    pygame.draw.circle(VENTANA, (255, 255, 0), CENTRO, 80)

    pygame.draw.circle(VENTANA, (252, 34, 0), (CENTRO[0]+200,CENTRO[1]), 3)
    pygame.draw.circle(VENTANA, (197, 149, 0), (CENTRO[0]+300,CENTRO[1]), 6)

    pygame.draw.circle(VENTANA, (28, 156, 0), (CENTRO[0]+400,CENTRO[1]), 10)










    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            ejecutar = False

    pygame.display.update()


pygame.quit()
