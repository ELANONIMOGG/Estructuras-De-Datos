from TDA_pila import Pila 

def es_operador(caracter):
    return caracter in ["(",")","^","*","/","+","-"]

def prioridad(caracter):
    if caracter in ["^"]:
        x = 3 
    elif caracter in ["*","/"]:
        x = 2
    elif caracter in ["+","-"]:
        x = 1
    else:
        x = 0
    return x

expresion_salida = ""
pila_operadores = Pila()

cadena = input("Expresion: ")

for caracter in cadena:
    if not es_operador(caracter):
        expresion_salida += caracter
    else:
        if caracter in ["("]:
            pila_operadores.insertar(caracter)    
        elif caracter in [")"]:
            while not pila_operadores.pila_vacia() and pila_operadores.tope_pila() not in ["("] :
                operador = pila_operadores.quitar()
                expresion_salida += operador
            operador = pila_operadores.quitar()
        else:
            while not pila_operadores.pila_vacia() and prioridad(caracter) <= prioridad(pila_operadores.tope_pila):
                operador = pila_operadores.quitar()
                expresion_salida += operador
            pila_operadores.insertar(caracter)

while not pila_operadores.pila_vacia():
    operador = pila_operadores.quitar()
    expresion_salida += operador    

print("La expresion en postfijo es: ", expresion_salida)  