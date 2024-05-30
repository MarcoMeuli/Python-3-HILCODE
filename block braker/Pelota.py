# CLASE PELOTA

def constructor(color, x, y, velocidad, radio):
    objeto = dict()

    objeto["tipo"] = "pelota"
    setColor(objeto, color)
    setX(objeto, x)
    setY(objeto, y)
    setVelocidad(objeto, velocidad)
    setRadio(objeto, radio)


    return objeto


def checkTipo(objeto):
    return True if "tipo" in objeto and objeto["tipo"] == "pelota" else False




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




def getX(objeto):
    if checkTipo(objeto):
        return objeto["x"]
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen x.")
    else:
        print("El objeto pasado como parametro no posee tipo")
    return None

def setX(objeto, nuevoX):
    if not type(nuevoX) in (int, float):
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
    if not type(nuevoY) in (int, float):
        print("ERROR: La y debe ser un entero.")
        return


    if checkTipo(objeto):
        objeto["y"] = nuevoY
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen y.")
    else:
        print("El objeto pasado como parametro no posee y")




def getVelocidad(objeto):
    if checkTipo(objeto):
        return objeto["velocidad"]
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen velocidad.")
    else:
        print("El objeto pasado como parametro no posee tipo")
    return None

def setVelocidad(objeto, nuevoVelocidad):

    if checkTipo(objeto):
        objeto["velocidad"] = nuevoVelocidad
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen velocidad.")
    else:
        print("El objeto pasado como parametro no posee velocidad")



def getRadio(objeto):
    if checkTipo(objeto):
        return objeto["radio"]
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen radio.")
    else:
        print("El objeto pasado como parametro no posee tipo")
    return None

def setRadio(objeto, nuevoRadio):

    if checkTipo(objeto):
        objeto["radio"] = nuevoRadio
    elif "tipo" in objeto:
        print(f"Los objetos de tipo {objeto['tipo']}, no tienen radio.")
    else:
        print("El objeto pasado como parametro no posee radio")
