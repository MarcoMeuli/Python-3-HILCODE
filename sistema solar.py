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


x_mercurio = 60
y_mercurio = CENTRO[1]
radio_mercurio = 150
angulo_mercurio = 0
velocidad_angular_mercurio = 0.02

x_venus = 60
y_venus = CENTRO[1]
radio_venus = 90
angulo_venus = 0
velocidad_angular_venus = 0.16

x_tierra = 380
y_tierra = CENTRO[1]
radio_tierra = 150
angulo_tierra = 0
velocidad_angular_tierra = 0.01

x_marte = 380
y_marte = CENTRO[1]
radio_marte = 180
angulo_marte = 0
velocidad_angular_marte = 0.0052

x_jupiter = 380
y_marte = CENTRO[1]
radio_jupiter = 250
angulo_jupiter = 0
velocidad_angular_jupiter = 0.0008

x_saturno = 380
y_saturno = CENTRO[1]
radio_saturno = 350
angulo_saturno = 0
velocidad_angular_saturno = 0.0003

x_urano = 380
y_urano = CENTRO[1]
radio_urano = 450
angulo_urano = 0
velocidad_angular_urano = 0.0001


ejecutar = True
while ejecutar == True:
    VENTANA.fill((0,0,0))
    pygame.draw.circle(VENTANA, (255, 255, 0), CENTRO, 50)

    pygame.draw.circle(VENTANA, (252, 100, 0), (CENTRO[0]+60,CENTRO[1]), 3)
    pygame.draw.circle(VENTANA, (197, 149, 0), (CENTRO[0]+90,CENTRO[1]), 6)
    pygame.draw.circle(VENTANA, (28, 156, 0), (x_tierra,y_tierra), 10)
    pygame.draw.circle(VENTANA, (252, 34, 0), (CENTRO[0]+180,CENTRO[1]), 12)
    pygame.draw.circle(VENTANA, (255, 255, 50), (CENTRO[0]+250,CENTRO[1]), 28)
    pygame.draw.circle(VENTANA, (252, 200, 0), (CENTRO[0]+350,CENTRO[1]), 18)
    pygame.draw.circle(VENTANA, (255, 255, 100), (CENTRO[0]+450,CENTRO[1]), 15)
    pygame.draw.circle(VENTANA, (0, 100, 255), (CENTRO[0]+500,CENTRO[1]), 8)

    angulo_tierra += velocidad_angular_tierra
    x_tierra,y_tierra = movimiento(radio_tierra, CENTRO[0], CENTRO[1], angulo_tierra)



#VEL DE PLANETAS: 0.02, 0.16, 0.1, 0.0052, 0.0008, 0.0003, 0.0001, 0.0006








    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            ejecutar = False

    pygame.display.update()


pygame.quit()
