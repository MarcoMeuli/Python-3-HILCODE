# TEST GET Y SET

import Bloque
import Pelota
import Plataforma


def main():
    bloque1 = Bloque.constructor(color=(10,10,10), ancho=150, alto=240, x=325, y=123, estado=3)
    print("Bloque:")
    print("Get color:", Bloque.getColor(bloque1))
    print("Get ancho:", Bloque.getAncho(bloque1))
    print("Get alto:", Bloque.getAlto(bloque1))
    print("Get x:", Bloque.getX(bloque1))
    print("Get y:", Bloque.getY(bloque1))
    print("Get estado:", Bloque.getEstado(bloque1))


    plataforma1 = Plataforma.constructor(color=(222,50,20), ancho=78, alto=45, x=85, y=23, velocidad=3)
    print("\nPlataforma:")
    print("Get color:", Plataforma.getColor(plataforma1))
    print("Get ancho:", Plataforma.getAncho(plataforma1))
    print("Get alto:", Plataforma.getAlto(plataforma1))
    print("Get x:", Plataforma.getX(plataforma1))
    print("Get y:", Plataforma.getY(plataforma1))
    print("Get velocidad:", Plataforma.Velocidad(plataforma1))
