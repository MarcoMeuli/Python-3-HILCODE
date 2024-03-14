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


def crearTabla():
    tabla = list()
    num = 1

    for i in range(3):
        fila = list()

        for i in range(3):
            fila.append(num)
            num += 1
        tabla.append(fila)
    return tabla


def cambiar_posiciones(tabla, posicion):
    i = 0
    encontrado = False
    while i < len(tabla) and not encontrado:
        j = 0
        while j < len(tabla[i]):
            if tabla[i][j] == posicion:
                tabla[i][j] = jugada[0]
                dibujos(posicion)
                encontrado = True
            elif type(tabla[i][j]) == int and tabla[i][j] > posicion:
                encontrado = True
            j+=1
        i+=1


def dibujos(posicion):
    if jugada[0] == "X":
        r1, r2 = posiciones_x(posicion)
        dibujar_x(r1,r2)
        jugada[0] = "O"

    elif jugada[0] == "O":
        centro = posiciones_o(posicion)
        dibujar_o(centro)
        jugada[0] = "X"

jugada = ["X"]


def victoria(tabla):
    ganador = False
    if tabla[0][0] == tabla[0][1] and tabla[0][0] == tabla[0][2]: ganador = tabla[0][0]
    elif tabla[1][0] == tabla[1][1] and tabla[1][0] == tabla[1][2]: ganador = tabla[1][0]
    elif tabla[2][0] == tabla[2][1] and tabla[2][0] == tabla[2][2]: ganador = tabla[2][0]
    elif tabla[0][0] == tabla[1][0] and tabla [0][0] == tabla[2][0]: ganador = tabla[0][0]
    elif tabla[0][1] == tabla[1][1] and tabla[0][1] == tabla[2][1]: ganador = tabla[0][1]
    elif tabla[0][2] == tabla[1][2] and tabla[0][2] == tabla[2][2]: ganador = tabla[0][2]
    elif tabla[0][0] == tabla[1][1] and tabla[0][0] == tabla[2][2]: ganador = tabla[0][0]
    elif tabla[0][2] == tabla[1][1] and tabla[0][2] == tabla[2][0]: ganador = tabla[0][2]
    else:
        i=0
        j=0
        interrumpir = False
        while i < len(tabla[i]) and not interrumpir:
            j=0
            while j < len(tabla[i]):
                if type(tabla[i][j]) == int:
                    interrumpir = True
                elif i == 2 and j == 2:
                    interrumpir = True
                    ganador = "Empate"
                j+=1
            i+=1

    return ganador

dibujar_tabla()
tabla = crearTabla()
ganador = victoria(tabla)

run = True
while run:
    while not(ganador in ("X","O","Empate")) and run:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                posicion = click(evento.pos)
                cambiar_posiciones(tabla=tabla, posicion=posicion)
                ganador = victoria(tabla)
                print("WINNER:", ganador)
        pygame.display.update()

pygame.quit()
