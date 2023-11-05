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


x_mercurio = CENTRO[0]+40
y_mercurio = CENTRO[1]
radio_mercurio = 40
angulo_mercurio = 0
velocidad_angular_mercurio = 0.002

x_venus = CENTRO[0]+190
y_venus = CENTRO[1]
radio_venus = 90
angulo_venus = 0
velocidad_angular_venus = 0.016

x_tierra = CENTRO[0]+150
y_tierra = CENTRO[1]
radio_tierra = 150
angulo_tierra = 0
velocidad_angular_tierra = 0.01

x_marte = CENTRO[0]+180
y_marte = CENTRO[1]
radio_marte = 180
angulo_marte = 0
velocidad_angular_marte = 0.00052

x_jupiter = CENTRO[0]+250
y_jupiter = CENTRO[1]
radio_jupiter = 250
angulo_jupiter = 0
velocidad_angular_jupiter = 0.00008

x_saturno = CENTRO[0]+350
y_saturno = CENTRO[1]
radio_saturno = 350
angulo_saturno = 0
velocidad_angular_saturno = 0.00003

x_urano = CENTRO[0]+450
y_urano = CENTRO[1]
radio_urano = 450
angulo_urano = 0
velocidad_angular_urano = 0.00001

x_neptuno = CENTRO[0]+500
y_neptuno = CENTRO[1]
radio_neptuno = 500
angulo_neptuno = 0
velocidad_angular_neptuno = 0.00006



ejecutar = True
while ejecutar == True:
    VENTANA.fill((0,0,0))
    pygame.draw.circle(VENTANA, (255, 255, 0), CENTRO, 50)

    pygame.draw.circle(VENTANA, (252, 100, 0), (x_mercurio,y_mercurio), 3)
    pygame.draw.circle(VENTANA, (197, 149, 0), (x_venus,y_venus), 6)
    pygame.draw.circle(VENTANA, (28, 156, 0), (x_tierra,y_tierra), 10)
    pygame.draw.circle(VENTANA, (252, 34, 0), (x_marte,y_marte), 12)
    pygame.draw.circle(VENTANA, (255, 255, 50), (x_jupiter,y_jupiter), 28)
    pygame.draw.circle(VENTANA, (252, 200, 0), (x_saturno,y_saturno), 18)
    pygame.draw.circle(VENTANA, (255, 255, 100), (x_urano,y_urano), 15)
    pygame.draw.circle(VENTANA, (0, 100, 255), (x_neptuno,y_neptuno), 8)


    angulo_mercurio += velocidad_angular_mercurio
    x_mercurio,y_mercurio = movimiento(radio_mercurio, CENTRO[0], CENTRO[1], angulo_mercurio)

    angulo_venus += velocidad_angular_venus
    x_mercurio,y_venus = movimiento(radio_venus, CENTRO[0], CENTRO[1], angulo_venus)

    angulo_tierra += velocidad_angular_tierra
    x_tierra,y_tierra = movimiento(radio_tierra, CENTRO[0], CENTRO[1], angulo_tierra)

    angulo_marte += velocidad_angular_marte
    x_marte,y_marte = movimiento(radio_marte, CENTRO[0], CENTRO[1], angulo_marte)

    angulo_jupiter += velocidad_angular_jupiter
    x_jupiter,y_jupiter = movimiento(radio_jupiter, CENTRO[0], CENTRO[1], angulo_jupiter)

    angulo_saturno += velocidad_angular_saturno
    x_saturno,y_saturno = movimiento(radio_saturno, CENTRO[0], CENTRO[1], angulo_saturno)

    angulo_urano += velocidad_angular_urano
    x_urano,y_urano = movimiento(radio_urano, CENTRO[0], CENTRO[1], angulo_urano)

    angulo_neptuno += velocidad_angular_neptuno
    x_neptuno,y_neptuno = movimiento(radio_neptuno, CENTRO[0], CENTRO[1], angulo_neptuno)


#VEL DE PLANETAS: 0.02, 0.16, 0.1, 0.0052, 0.0008, 0.0003, 0.0001, 0.0006








    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            ejecutar = False

    pygame.display.update()


pygame.quit()
