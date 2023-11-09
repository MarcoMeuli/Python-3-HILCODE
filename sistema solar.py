import pygame
import math
import random

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



x_mercurio = CENTRO[0]+50
y_mercurio = CENTRO[1]
radio_mercurio = 50
angulo_mercurio = 0
velocidad_angular_mercurio = 0.008

x_venus = CENTRO[0]+100
y_venus = CENTRO[1]
radio_venus = 100
angulo_venus = 0
velocidad_angular_venus = 0.006

x_tierra = CENTRO[0]+150
y_tierra = CENTRO[1]
radio_tierra = 150
angulo_tierra = 0
velocidad_angular_tierra = 0.004

x_marte = CENTRO[0]+200
y_marte = CENTRO[1]
radio_marte = 200
angulo_marte = 0
velocidad_angular_marte = 0.002

x_jupiter = CENTRO[0]+250
y_jupiter = CENTRO[1]
radio_jupiter = 250
angulo_jupiter = 0
velocidad_angular_jupiter = 0.0008

x_saturno = CENTRO[0]+300
y_saturno = CENTRO[1]
radio_saturno = 300
angulo_saturno = 0
velocidad_angular_saturno = 0.0006

x_urano = CENTRO[0]+350
y_urano = CENTRO[1]
radio_urano = 350
angulo_urano = 0
velocidad_angular_urano = 0.0004

x_neptuno = CENTRO[0]+400
y_neptuno = CENTRO[1]
radio_neptuno = 400
angulo_neptuno = 0
velocidad_angular_neptuno = 0.0002

x_luna = CENTRO[0]
y_luna = CENTRO[1]
radio_luna = 15
angulo_luna = 0
velocidad_angular_luna = 0.01

x_anillos = CENTRO[0]
y_anillos = CENTRO[1]
radio_anillos = 25
angulo_anillos = 0
velocidad_angular_anillos = 0.01

ejecutar = True
while ejecutar == True:
    VENTANA.fill((0,0,0))
    pygame.draw.circle(VENTANA, (255, 255, 0), CENTRO, 35)

    pygame.draw.circle(VENTANA, (162, 162, 162), (x_mercurio,y_mercurio), 3)
    pygame.draw.circle(VENTANA, (228, 163, 98), (x_venus,y_venus), 6)
    pygame.draw.circle(VENTANA, (28, 156, 0), (x_tierra,y_tierra), 10)
    pygame.draw.circle(VENTANA, (252, 34, 0), (x_marte,y_marte), 12)
    pygame.draw.circle(VENTANA, (131, 48, 21), (x_jupiter,y_jupiter), 23)
    pygame.draw.circle(VENTANA, (252, 200, 0), (x_saturno,y_saturno), 18)
    pygame.draw.circle(VENTANA, (107, 217, 255), (x_urano,y_urano), 15)
    pygame.draw.circle(VENTANA, (0, 100, 255), (x_neptuno,y_neptuno), 8)

    pygame.draw.circle(VENTANA, (160, 160, 160), (x_luna,y_luna), 2)


    pygame.draw.circle(VENTANA, (255, 255, 255), (x_anillos,y_anillos), 3)
    velocidad_angular_anillos = 0.01
    pygame.draw.circle(VENTANA, (255, 255, 255), (x_anillos,y_anillos), 3)
    velocidad_angular_anillos = 0.03
    pygame.draw.circle(VENTANA, (255, 255, 255), (x_anillos,y_anillos), 3)
    velocidad_angular_anillos = 0.05
    pygame.draw.circle(VENTANA, (255, 255, 255), (x_anillos,y_anillos), 3)
    velocidad_angular_anillos = 0.07
    pygame.draw.circle(VENTANA, (255, 255, 255), (x_anillos,y_anillos), 3)
    velocidad_angular_anillos = 0.09
    pygame.draw.circle(VENTANA, (255, 255, 255), (x_anillos,y_anillos), 3)
    velocidad_angular_anillos = 0.11
    pygame.draw.circle(VENTANA, (255, 255, 255), (x_anillos,y_anillos), 3)



    angulo_mercurio += velocidad_angular_mercurio
    x_mercurio,y_mercurio = movimiento(radio_mercurio, CENTRO[0], CENTRO[1], angulo_mercurio)

    angulo_venus += velocidad_angular_venus
    x_venus,y_venus = movimiento(radio_venus, CENTRO[0], CENTRO[1], angulo_venus)

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

    angulo_luna += velocidad_angular_luna
    x_luna,y_luna = movimiento(radio_luna, x_tierra, y_tierra, angulo_luna)

    angulo_anillos += velocidad_angular_anillos
    x_anillos,y_anillos = movimiento(radio_anillos, x_saturno, y_saturno, angulo_anillos)




    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            ejecutar = False

    pygame.display.update()


pygame.quit()
