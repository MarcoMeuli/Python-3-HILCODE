import pygame
from colores import *
import random
ANCHO = 300
ALTO = 400
ANCHO_RAYA = 100
NOMBRE = "Tic Tac Toe"

VENTANA = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption(NOMBRE)

VENTANA.fill((getColor("BLANCO")))

def dibujar_tabla():
    for i in range(1,4):
        # LINEAS HORIZONTALES
        pygame.draw.line(surface = VENTANA,
                        color = getColor("ROJO"),
                        width = 3,
                        start_pos = (0,i*ANCHO_RAYA),
                        end_pos = (ANCHO,i*ANCHO_RAYA))

        # LINEAS VERTICALES
        pygame.draw.line(surface = VENTANA,
                        color = getColor("ROJO"),
                        width = 3,
                        start_pos = (i*ANCHO_RAYA,0),
                        end_pos = (i*ANCHO_RAYA,ANCHO))

def dibujar_x(r1, r2):
    pygame.draw.line(surface = VENTANA,
                    color = getColor("ROJO"),
                    width = 3,
                    start_pos = r1[0],
                    end_pos = r1[1])

    pygame.draw.line(surface = VENTANA,
                    color = getColor("ROJO"),
                    width = 3,
                    start_pos = r2[0],
                    end_pos = r2[1])

def dibujar_o(centro):
    pygame.draw.circle(surface = VENTANA,
                    color = getColor("ROJO"),
                    width = 3,
                    radius = 50,
                    center = centro)


def posiciones_o(posicion):
    posiciones = [ [    [1,2,3],
                        [4,5,6],
                        [7,8,9]],

                    [   [50,150,250],
                        [50,150,250],
                        [50,150,250]],

                    [   [50,50,50],
                        [150,150,150],
                        [250,250,250]]         ]

    for i in range(len(posiciones[0])):
        for j in range(len(posiciones[0][i])):
            if posiciones[0][i][j] == posicion:
                I = i
                J = j
                break
    x = posiciones[1][I][J]
    y = posiciones[2][I][J]
    return (x, y)




def posiciones_x(posicion):
    posiciones = {  1: ([(0,0),(100,100)],[(0,100),(100,0)]),
                    2: ([(100,0),(200,100)], [(100,100),(200,0)]),
                    3: ([(200,0),(300,100)], [(200,100),(300,0)]),
                    4: ([(0,100),(100,200)], [(0,200),(100,100)]),
                    5: ([(100,100),(200,200)], [(100,200),(200,100)]),
                    7: ([(0,200),(100,300)], [(0,300),(100,200)]),
                    6: ([(200,100),(300,200)], [(200,200),(300,100)]),
                    8: ([(100,200),(200,300)],[(100,300),(200,200)]),
                    9: ([(200,200),(300,300)],[(200,300),(300,200)])    }



    r1 = posiciones[posicion][0]
    r2 = posiciones[posicion][1]
    return r1, r2

def click(mouse_pos):
    if (mouse_pos[0] > 0 and mouse_pos[0] < 100) and (mouse_pos[1] > 0 and mouse_pos[1] < 100): return 1
    elif (mouse_pos[0] > 100 and mouse_pos[0] < 200) and (mouse_pos[1] > 0 and mouse_pos[1] < 100): return 2
    elif (mouse_pos[0] > 200 and mouse_pos[0] < 300) and (mouse_pos[1] > 0 and mouse_pos[1] < 100): return 3
    elif (mouse_pos[0] > 0 and mouse_pos[0] < 100) and (mouse_pos[1] > 100 and mouse_pos[1] < 200): return 4
    elif (mouse_pos[0] > 100 and mouse_pos[0] < 200) and (mouse_pos[1] > 100 and mouse_pos[1] < 200): return 5
    elif (mouse_pos[0] > 200 and mouse_pos[0] < 300) and (mouse_pos[1] > 100 and mouse_pos[1] < 200): return 6
    elif (mouse_pos[0] > 0 and mouse_pos[0] < 100) and (mouse_pos[1] > 200 and mouse_pos[1] < 300): return 7
    elif (mouse_pos[0] > 100 and mouse_pos[0] < 200) and (mouse_pos[1] > 200 and mouse_pos[1] < 300): return 8
    elif (mouse_pos[0] > 200 and mouse_pos[0] < 300) and (mouse_pos[1] > 200 and mouse_pos[1] < 300): return 9
    else: return None


def turno():
    ran = random.randint(0,1)
    if ran == 0: return "x"
    else: return "o"


def crearCasillasUsadas():
    tabla = list()
    num = 1

    for i in range(3):
        fila = list()

        for i in range(3):
            fila.append(num)
            num += 1
        tabla.append(fila)

    return tabla


def cambiar_posiciones(casillasUsadas, posicion):

    for i in range(len(casillasUsadas[0])):
        for j in range(len(casillasUsadas[0][i])):
            if casillasUsadas[0][i][j] == posicion and tabla[i][j] == " ":
                # COSAS #
                tabla[i][j] = jugada[0]
                break

dibujar_tabla()
turno = turno()
casillasUsadas = crearCasillasUsadas()
run = True
while run:

    print(casillasUsadas)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False


        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos_click = click(evento.pos)

            if turno == "x":
                x, y = posiciones_x(posicion=pos_click)
                dibujar_x(x,y)
                turno = "o"


            elif turno == "o":
                pos = posiciones_o(posicion=pos_click)
                dibujar_o(pos)
                turno = "x"

            casillasUsadas.append(pos)


    pygame.display.update()

pygame.quit()


