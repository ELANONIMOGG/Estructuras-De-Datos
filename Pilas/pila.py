"""
from TDA_pila import Pila 
import random

pila1 = Pila()
pila2 = Pila()

def busca(dato):
    encontrado = False
    while not pila1.pila_vacia() and dato != pila1.tope_pila():
        pila2.insertar(pila1.quitar())
    if not pila1.pila_vacia():
        encontrado = True
    else:
        encontrado = False

    while not pila2.pila_vacia():
        pila1.insertar(pila2.quitar())
    
    return encontrado


def cuenta(dato):
    acumulador = 0
    while not pila1.pila_vacia() :
        x = pila1.quitar()
        if x == dato :
            acumulador += 1
        pila2.insertar(x)

    while not pila2.pila_vacia():
        pila1.insertar(pila2.quitar())

    return acumulador
"""
#for i in range (10):
#   pila1.insertar(random.randint(0,200))

"""

pila1.insertar(2)
pila1.insertar(2)
pila1.insertar(2)
pila1.insertar(2.0)
pila1.insertar(3) 

print("El 2 se encuentra",cuenta(2)," Veces")
print("El 3 se encuentra",cuenta(3)," Veces")
print("El 10 se encuentra",cuenta(10)," Veces")



"""

"""
from TDA_pila import Pila 
import random

pila1 = Pila()
pila2 = Pila()

def busca(dato):
    encontrado = False
    posicion_desde_tope = 0
    posicion_desde_fondo = 0

    while not pila1.pila_vacia() and dato != pila1.tope_pila():
        pila2.insertar(pila1.quitar())
        posicion_desde_fondo += 1

    if not pila1.pila_vacia():
        encontrado = True
        # Calculando la posición desde el tope de la pila
        while not pila2.pila_vacia():
            pila1.insertar(pila2.quitar())
            posicion_desde_tope += 1
    else:
        encontrado = False

    while not pila2.pila_vacia():
        pila1.insertar(pila2.quitar())

    return encontrado, posicion_desde_tope, posicion_desde_fondo



def cuenta(dato):
    acumulador = 0
    while not pila1.pila_vacia() :
        x = pila1.quitar()
        if x == dato :
            acumulador += 1
        pila2.insertar(x)

    while not pila2.pila_vacia():
        pila1.insertar(pila2.quitar())

    return acumulador

pila1.insertar(2)
pila1.insertar(2)
pila1.insertar(2)
pila1.insertar(2.0)
pila1.insertar(3) 

print("El 2 se encuentra",cuenta(2)," Veces")
print("El 3 se encuentra",cuenta(3)," Veces")
print("El 10 se encuentra",cuenta(10)," Veces")

elemento = 3
encontrado, posicion_tope, posicion_fondo = busca(elemento)
if encontrado:
    print("El elemento", elemento, "se encuentra en la posición", posicion_tope, "desde el tope y en la posición", posicion_fondo, "desde el fondo de la pila.")
else:
    print("El elemento", elemento, "no se encuentra en la pila.")
"""
from TDA_pila import Pila 
import random

pila1 = Pila()
pila2 = Pila()

def busca(dato):
    encontrado = False
    while not pila1.pila_vacia() and dato != pila1.tope_pila():
        pila2.insertar(pila1.quitar())
    if not pila1.pila_vacia():
        encontrado = True
    else:
        encontrado = False

    while not pila2.pila_vacia():
        pila1.insertar(pila2.quitar())
    
    return encontrado


def cuenta(dato):
    acumulador = 0
    while not pila1.pila_vacia() :
        x = pila1.quitar()
        if x == dato :
            acumulador += 1
        pila2.insertar(x)

    while not pila2.pila_vacia():
        pila1.insertar(pila2.quitar())

    return acumulador
"""
#for i in range (10):
#   pila1.insertar(random.randint(0,200))

"""
def posicion(dato):
    ct = 0
    cf = 0

    if busca(dato):
        while not pila1.pila_vacia() and dato != pila1.tope_pila():
            pila2.insertar(pila1.quitar())
            ct += 1
        pila2.insertar(pila1.quitar())

        while not pila1.pila_vacia():
            pila2.insertar(pila1.quitar())
            cf += 1
        while not pila2.pila_vacia():
            pila1.insertar(pila2.quitar())
        

    return ct, cf







pila1.insertar(1)
pila1.insertar(7)
pila1.insertar(30)
pila1.insertar(90)
pila1.insertar(8)
pila1.insertar(150)
pila1.insertar(19)
pila1.insertar(14)
pila1.insertar(77) 

print(pila1.imprime())
t,f = posicion(90)
print("El dato se encuentra",t," debajo del tope y ",f,"arriba del fondo")





