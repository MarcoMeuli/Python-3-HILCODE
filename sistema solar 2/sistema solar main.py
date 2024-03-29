import planets_utils
import pygame
import math
import random

ANCHO = 1600
ALTO = 900
CENTRO = (ANCHO/2, ALTO/2)
NOMBRE = "sistema solar"
N_ASTEROIDES= 1000
N_ANILLOS= 100
ejecutar= True



VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(NOMBRE)

def movimiento(radio, centro_x, centro_y, angulo):
    x = centro_x + int(math.cos(angulo)*radio)
    y = centro_y + int(math.sin(angulo)*radio)
    return x, y


sol = planets_utils.constructorPlanetas(nombre="sol", tam=35, x=CENTRO[0], y=CENTRO[1], radio=0, color=(255,255,0))
mercurio = planets_utils.constructorPlanetas(nombre="mercurio", tam=3, radio=45, color=(162,162,162))
venus = planets_utils.constructorPlanetas(nombre="venus", tam=6, radio=60, color=(228,163,98))
tierra = planets_utils.constructorPlanetas(nombre="tierra", tam=10, radio=90, color=(28,156,0))
marte = planets_utils.constructorPlanetas(nombre="marte", tam=12, radio=125, color=(252,34,0))
jupiter = planets_utils.constructorPlanetas(nombre="jupiter", tam=23, radio=260, color=(131,48,21))
saturno = planets_utils.constructorPlanetas(nombre="saturno", tam=18, radio=320, color=(204,102,0))
urano = planets_utils.constructorPlanetas(nombre="urano", tam=15, radio=370, color=(107,217,255))
neptuno = planets_utils.constructorPlanetas(nombre="neptuno", tam=8, radio=400, color=(0,100,255))
luna = planets_utils.constructorPlanetas(nombre="luna", tam=2, radio=20, color=(200,200,200))
planetas = [sol, mercurio, venus, tierra, marte, jupiter, saturno, urano, neptuno, luna]

for i in range(N_ASTEROIDES):
    planetas.append(planets_utils.constructorPlanetas(nombre="asteroides", tam=random.randint(1,3), radio=random.randint(150, 220), color=(255,255,255)))
for i in range(N_ANILLOS):
    planetas.append(planets_utils.constructorPlanetas(nombre="anillos", tam=random.randint(10,16)/10, radio=random.randint(23,28), color=(255,255,255)))

for i in range(len(planetas)):
    planetas[i] = planets_utils.setX(planetas[i], CENTRO[0] + planets_utils.getRadio(planetas[i]))
    planetas[i] = planets_utils.setY(planetas[i], CENTRO[1])
    if planets_utils.getNombre(planetas[i])== "asteroides" or planets_utils.getNombre(planetas[i])== "anillos":
        planetas[i] = planets_utils.setAngulo(planetas[i], random.randint(0,1000))

while ejecutar == True:
    VENTANA.fill((0,0,0))

    for i in range(len(planetas)):
        pygame.draw.circle(VENTANA,
            planets_utils.getColor(planetas[i]),
            (planets_utils.getX(planetas[i]),
            planets_utils.getY(planetas[i])),
            planets_utils.getTam(planetas[i]))



        if planets_utils.getNombre(planetas[i]) == "luna":
            x, y = movimiento(radio = planets_utils.getRadio(planetas[i]),
            centro_x = tierra["x"],
            centro_y = tierra["y"],
            angulo = planets_utils.getAngulo(planetas[i]))

        elif planets_utils.getNombre(planetas[i]) == "anillos":
            x, y = movimiento(radio = planets_utils.getRadio(planetas[i]),
            centro_x = saturno["x"],
            centro_y = saturno["y"],
            angulo = planets_utils.getAngulo(planetas[i]))

        else:
            x, y = movimiento(radio = planets_utils.getRadio(planetas[i]),
            centro_x = CENTRO[0],
            centro_y = CENTRO[1],
            angulo = planets_utils.getAngulo(planetas[i]))


        planetas[i] = planets_utils.setX(planetas[i], x)
        planetas[i] = planets_utils.setY(planetas[i], y)


        nuevo_angulo = planets_utils.getVelocidad(planetas[i]) + planets_utils.getAngulo(planetas[i])
        planetas[i] = planets_utils.setAngulo(planetas[i], nuevo_angulo)


    for eventos in pygame.event.get():
        if eventos.type == pygame.MOUSEBUTTONDOWN and eventos.button == 4:
            for i in range(len(planetas)):
                planetas[i]["tam"]+=planetas[i]["tam"]/10
                planetas[i]["radio"]+=planetas[i]["radio"]/10

        if eventos.type == pygame.MOUSEBUTTONDOWN and eventos.button == 5:
            for i in range(len(planetas)):
                planetas[i]["tam"]-=planetas[i]["tam"]/10
                planetas[i]["radio"]-=planetas[i]["radio"]/10

        if eventos.type == pygame.KEYDOWN:
            if eventos.key == pygame.K_ESCAPE:
                ejecutar = False

        if eventos.type == pygame.QUIT:
            ejecutar = False

    pygame.display.update()
pygame.quit()
