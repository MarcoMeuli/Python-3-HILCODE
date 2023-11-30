import random

#defino el constructor de planetas
def constructorPlanetas(nombre,tam, radio, color, x=0, y=0, angulo=0, v_angular=None):
    v_angular = setVelocidad(nombre=nombre)
    objeto = {
            "nombre": nombre,
            "tam": tam,
            "radio": radio,
            "angulo": angulo,
            "v_angular": v_angular,
            "x": x,
            "y": y,
            "color": color,
            "tipo": "planeta"
            }
    return objeto




#########
#########
def setNombre(objeto, nombre):
    if "nombre" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        objeto["nombre"] = nombre
        return  objeto
    elif type(nombre) == str:
        objeto["nombre"] = nombre
        return  objeto
    else:
        return None

def getNombre(objeto):
    return objeto["nombre"]




def setTam(objeto, tam):
    if "tam" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        objeto["tam"] = tam
    elif tam <= 0:
        objeto["tam"] = tam
    else:
        print("Objeto invalido.")
    return objeto

def getTam(objeto):
    return objeto["tam"]




def setRadio(objeto, radio):
    if "radio" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        objeto["radio"] = radio
    elif tam <= 0:
        objeto["radio"] = radio
    else:
        print("Objeto invalido.")
    return objeto

def getRadio(objeto):
    return objeto["radio"]




def setVelocidad(objeto=None, nombre=None):
    velocidad = None
    astros = {
            "sol": 0,
            "mercurio": 0.008,
            "venus": 0.006,
            "tierra": 0.004,
            "marte": 0.002,
            "jupiter": 0.0008,
            "saturno": 0.0006,
            "urano": 0.0004,
            "neptuno": 0.0002
            }
    if nombre != None and nombre in astros and objeto == None:
        velocidad = astros[nombre]
        return velocidad
    elif nombre not in astros and nombre == None:
        velocidad = 0.3/random.randint(1,100)
        return velocidad
    elif "tipo" in objeto and "nombre" in objeto and objeto["tipo"] == "planeta":
        objeto["v_angular"] = nueva_velocidad
        return velocidad
    else:
        print("Objeto invalido.")
    return objeto

def getVelocidad(objeto):
    if "v_angular" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        return objeto["v_angular"]
    else:
        print("Objeto invalido.")
    return objeto




def setX(objeto, x):
    if "x" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        objeto["x"] = x
    else:
        print("Objeto invalido.")
    return objeto

def getX(objeto):
    return objeto["x"]




def setY(objeto, y):
    if "y" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        objeto["y"] = y
    else:
        print("Objeto invalido.")
    return objeto

def getY(objeto):
    return objeto["y"]




def setAngulo(objeto, angulo):
    if "angulo" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        objeto["angulo"] = angulo
    elif angulo <= 0:
        objeto["angulo"] = angulo
    else:
        print("Objeto invalido.")
    return objeto

def getAngulo(objeto):
    return objeto["angulo"]
#########
#########







#creo los planetas:
mercurio = constructorPlanetas(nombre="mercurio", tam=3, radio=50, color=(162,162,162))
venus = constructorPlanetas(nombre="venus", tam=6, radio=100, color=(228,163,98))
tierra = constructorPlanetas(nombre="tierra", tam=10, radio=150, color=(28,156,0))
marte = constructorPlanetas(nombre="marte", tam=12, radio=200, color=(252,34,0))
jupiter = constructorPlanetas(nombre="jupiter", tam=23, radio=250, color=(131,48,21))
saturno = constructorPlanetas(nombre="saturno", tam=18, radio=300, color=(252,200,0))
urano = constructorPlanetas(nombre="urano", tam=15, radio=350, color=(107,217,255))
neptuno = constructorPlanetas(nombre="neptuno", tam=8, radio=400, color=(0,100,255))
_PC_ = {"RAM":8, "pantalla":"4K"}

print(getTam(objeto=mercurio))

