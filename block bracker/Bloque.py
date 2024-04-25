def constructor(color, ancho, alto, x, y, estado):
    objeto = {"color": color,
              "ancho": ancho,
              "alto": alto,
              "x": x,
              "y": y,
              "estado": estado,
              "tipo": "bloque"}
    return objeto




def getColor(objeto):
    if "tipo" in objeto and "color" in objeto and objeto["tipo"] == "bloque":
        return objeto["color"]
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen color.")
    else:
        print("El objeto pasado como parametro no posee tipo")
    return None

def setColor(objeto, nuevoColor):
    if type(nuevoColor) != tuple or len(nuevoColor) != 3:
        print("ERROR: El color debe estar en una tupla de tamanio 3.")
        return

    for i in nuevoColor:
        if i < 0 or i > 255 and i != int:
            print("ERROR: El color debe ser un entero entre 0-255.")
            return


    if "tipo" in objeto and "color" in objeto and objeto["tipo"] == "bloque":
        return objeto["color"]
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen color.")
    else:
        print("El objeto pasado como parametro no posee tipo")
    else:
        objeto["color"] = nuevoColor
    return objeto



def getAncho(objeto):
    if "tipo" in objeto and "ancho" in objeto and objeto["tipo"] == "bloque":
        return objeto["ancho"]
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen anchura.")
    else:
        print("El objeto pasado como parametro no posee tipo")
    return None

def setAncho(objeto, nuevoAncho):
    if nuevoAncho != int:
        print("ERROR: El ancho debe ser un entero.")


    if "tipo" in objeto and "ancho" in objeto and objeto["tipo"] == "bloque":
        return objeto["ancho"]
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen anchura.")
    else:
        print("El objeto pasado como parametro no posee tipo")



def getAlto(objeto):
    if "tipo" in objeto and "alto" in objeto and objeto["tipo"] == "bloque":
        return objeto["alto"]
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen altura.")
    else:
        print("El objeto pasado como parametro no posee tipo")
    return None

def setAlto(objeto, nuevoAlto):
    if nuevoAncho != int:
        print("ERROR: El alto debe ser un entero.")


    if "tipo" in objeto and "alto" in objeto and objeto["tipo"] == "bloque":
        return objeto["alto"]
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen altura.")
    else:
        print("El objeto pasado como parametro no posee tipo")



def getX(objeto):
    if "tipo" in objeto and "x" in objeto and objeto["tipo"] == "bloque":
        return objeto["x"]
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen x.")
    else:
        print("El objeto pasado como parametro no posee tipo")
    return None

def setX(objeto, nuevoX):
    if nuevoX != int:
        print("ERROR: La x debe ser un entero.")
        return


    if "tipo" in objeto and "x" in objeto and objeto["tipo"] == "bloque":
        return objeto["x"]
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen x.")
    else:
        print("El objeto pasado como parametro no posee tipo")
    else:
        objeto["x"] = nuevoColor
    return objeto



def getY(objeto):
    if "tipo" in objeto and "y" in objeto and objeto["tipo"] == "bloque":
        return objeto["y"]
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen y.")
    else:
        print("El objeto pasado como parametro no posee tipo")
    return None

def setY(objeto, nuevoY):
    if nuevoX != int:
        print("ERROR: La y debe ser un entero.")
        return


    if "tipo" in objeto and "y" in objeto and objeto["tipo"] == "bloque":
        return objeto["y"]
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen y.")
    else:
        print("El objeto pasado como parametro no posee tipo")
    else:
        objeto["y"] = nuevoColor
    return objeto
