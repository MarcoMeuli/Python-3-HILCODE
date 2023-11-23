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







def setNombre(objeto, nombre):
    return objeto["nombre"] = nombre

def getNombre(objeto):
    return objeto



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
    elif nombre not in astros and nombre == None:
        velocidad = 0.3/random.randint(1,100)
    elif "tipo" in objeto and "nombre" in objeto and objeto["tipo"] == "planeta":
        velocidad = astros[objeto["nombre"]]
    else:
        print("Objeto invalido.")
    return velocidad


def getVelocidad(objeto):
    if v_angular in objeto and objeto["tipo"] == "planeta":
        return objeto[v_angular]
    else:
        return None











#creo los planetas:
mercurio = constructorPlanetas(nombre="mercurio", tam=3, radio=50, color=(162,162,162))
venus = constructorPlanetas(nombre="venus", tam=6, radio=100, color=(228,163,98))
tierra = constructorPlanetas(nombre="tierra", tam=10, radio=150, color=(28,156,0))
marte = constructorPlanetas(nombre="marte", tam=12, radio=200, color=(252,34,0))
jupiter = constructorPlanetas(nombre="jupiter", tam=23, radio=250, color=(131,48,21))
saturno = constructorPlanetas(nombre="saturno", tam=18, radio=300, color=(252,200,0))
urano = constructorPlanetas(nombre="urano", tam=15, radio=350, color=(107,217,255))
neptuno = constructorPlanetas(nombre="neptuno", tam=8, radio=400, color=(0,100,255))


print(saturno)
