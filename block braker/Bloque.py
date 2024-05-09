# CLASE BLOQUE

def constructor(color, ancho, alto, x, y, estado):
    objeto = dict()

    objeto["tipo"] = "bloque"
    setColor(objeto, color)
    setAncho(objeto, ancho)
    setAlto(objeto, alto)
    setX(objeto, x)
    setY(objeto, y)
    setEstado(objeto, estado)


    return objeto


def checkTipo(objeto):
    return True if "tipo" in objeto and objeto["tipo"] == "bloque" else False




def getColor(objeto):
    if checkTipo(objeto):
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



    if checkTipo(objeto):
        objeto["color"] = nuevoColor
    elif "tipo" in objeto:
        print(f"El objeto de tipo {objeto['tipo']}, no tiene color.")
    else:
        print("El objeto pasado como parametro no posee color")






def getAncho(objeto):
    if checkTipo(objeto):
        return objeto["ancho"]
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen anchura.")
    else:
        print("El objeto pasado como parametro no posee tipo")
    return None

def setAncho(objeto, nuevoAncho):
    if type(nuevoAncho) != int:
        print("ERROR: El ancho debe ser un entero.")
        return


    if checkTipo(objeto):
        objeto["ancho"] = nuevoAncho
    elif "tipo" in objeto:
        print(f"El objeto de tipo {objeto['tipo']}, no tiene anchura.")
    else:
        print("El objeto pasado como parametro no posee anchura")



def getAlto(objeto):
    if checkTipo(objeto):
        return objeto["alto"]
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen altura.")
    else:
        print("El objeto pasado como parametro no posee tipo")
    return None

def setAlto(objeto, nuevoAlto):
    if type(nuevoAlto) != int:
        print("ERROR: El alto debe ser un entero.")
        return


    if checkTipo(objeto):
        objeto["alto"] = nuevoAlto
    elif "tipo" in objeto:
        print(f"El objeto de tipo {objeto['tipo']}, no tiene estado.")
    else:
        print("El objeto pasado como parametro no posee altura")



def getX(objeto):
    if checkTipo(objeto):
        return objeto["x"]
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen x.")
    else:
        print("El objeto pasado como parametro no posee tipo")
    return None

def setX(objeto, nuevoX):
    if type(nuevoX) != int:
        print("ERROR: La x debe ser un entero.")
        return


    if checkTipo(objeto):
        objeto["x"] = nuevoX
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen x.")
    else:
        print("El objeto pasado como parametro no posee x")







def getY(objeto):
    if checkTipo(objeto):
        return objeto["y"]
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen y.")
    else:
        print("El objeto pasado como parametro no posee tipo")
    return None

def setY(objeto, nuevoY):
    if type(nuevoY) != int:
        print("ERROR: La y debe ser un entero.")
        return


    if checkTipo(objeto):
        objeto["y"] = nuevoY
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen y.")
    else:
        print("El objeto pasado como parametro no posee y")



def getEstado(objeto):
    if checkTipo(objeto):
        return objeto["estado"]
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen estado.")
    else:
        print("El objeto pasado como parametro no posee estado")
    return None


def setEstado(objeto, nuevoEstado):
    if type(nuevoEstado) != int:
        print("ERROR: El estado debe ser un entero.")
        return


    if checkTipo(objeto):
        objeto["estado"] = nuevoEstado
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen estado.")
    else:
        print("El objeto pasado como parametro no posee estado")
