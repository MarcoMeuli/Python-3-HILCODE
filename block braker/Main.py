# MAIN

# importo las clases
import Bloque
import Pelota
import Plataforma

# importo herramientas
import random
import pygame
from colores import *
import Test
#Test.main() #Descomentar para hacer pruebas
pygame.init()




ANCHO, ALTO = 800, 600
pygame.display.set_caption("Block Breaker")
VENTANA = pygame.display.set_mode((ANCHO, ALTO))

plataforma = Plataforma.constructor(color=getColor("AZUL"), ancho=80, alto=20, x=400, y=570, velocidad=7)
pelota = Pelota.constructor(color=getColor("ROJO"),x=400, y=300, velocidad=7,radio=20)







VENTANA.fill(getColor("NEGRO"))
pygame.draw.rect(
            VENTANA,
            Plataforma.getColor(plataforma),
            (Plataforma.getX(plataforma),
            Plataforma.getY(plataforma),
            Plataforma.getAncho(plataforma),
            Plataforma.getAlto(plataforma)))

pygame.draw.circle(
            VENTANA,
            Pelota.getColor(pelota),
            (Pelota.getX(pelota),
            Pelota.getY(pelota)),
            Pelota.getRadio(pelota))

bloques = []
for i in range(10):
    bloques.append(Bloque.constructor(color=getColor("RANDOM"), ancho=80, alto=20, x=random.randint(0, 700), y=50, estado=1))
for i in range(10):
    pygame.draw.rect(
                VENTANA,
                Bloque.getColor(bloques[i]),
                (Bloque.getX(bloques[i]),
                Bloque.getY(bloques[i]),
                Bloque.getAncho(bloques[i]),
                Bloque.getAlto(bloques[i])))

pygame.display.update()
