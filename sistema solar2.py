#defino el constructor de planetas
def constructorPlanetas(nombre,tam, radio, v_angular, color, x=0, y=0, angulo=0):
    objeto = {
            "nombre": nombre,
            "tam": tam,
            "radio": radio,
            "angulo": angulo,
            "v_angular": v_angular,
            "x": x,
            "y": y,
            "color": color,
            "tipo": "planeta",
            }
    return objeto

#defino el set de velocidad
def setVelocidad(objeto):
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

    if objeto["tipo"] == "planeta":
        objeto["v_angular"] = astros[objeto["nombre"]]

    return velocidad

#creo los planetas:
mercurio = constructorPlanetas(nombre="mercurio", tam=3, radio=50, v_angular=0.008, color=(162,162,162))
venus = constructorPlanetas(nombre="venus", tam=6, radio=100, v_angular=0.006, color=(228,163,98))
tierra = constructorPlanetas(nombre="tierra", tam=10, radio=150, v_angular=0.004, color=(28,156,0))
marte = constructorPlanetas(nombre="marte", tam=12, radio=200, v_angular=0.002, color=(252,34,0))
jupiter = constructorPlanetas(nombre="jupiter", tam=23, radio=250, v_angular=0.0008, color=(131,48,21))
saturno = constructorPlanetas(nombre="saturno", tam=18, radio=300, v_angular=0.0006, color=(252,200,0))
urano = constructorPlanetas(nombre="urano", tam=15, radio=350, v_angular=0.0004, color=(107,217,255))
neptuno = constructorPlanetas(nombre="neptuno", tam=8, radio=400, v_angular=0.0002, color=(0,100,255))
