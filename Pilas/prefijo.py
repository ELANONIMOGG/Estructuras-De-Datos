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


pila_operandos = Pila()
pila_operadores = Pila()


cadena = input("Expresion: ")

for caracter in cadena:
    if not es_operador(caracter):
        pila_operandos.insertar(caracter)
    else:
        if caracter in ["("]:
            pila_operadores.insertar(caracter)    
        elif caracter in [")"]:
            while not pila_operadores.pila_vacia() and pila_operadores.tope_pila() not in ["("] :
                operando2 = pila_operandos.quitar()
                operando1 = pila_operandos.quitar()
                operador = pila_operadores.quitar()
                nuevo_operando = ""+operador+operando1+operando2
                pila_operandos.insertar(nuevo_operando)
            operador = pila_operadores.quitar()
        else:
            while not pila_operadores.pila_vacia() and prioridad(caracter) <= prioridad(pila_operadores.tope_pila):
                operando2 = pila_operadores.quitar()
                operando1 = pila_operadores.quitar()
                operador = pila_operadores.quitar()
                nuevo_operando = ""+operador+operando1+operando2
                pila_operandos.insertar(nuevo_operando)
            pila_operadores.insertar(caracter)

while not pila_operadores.pila_vacia():
    operando2 = pila_operandos.quitar()
    operando1 = pila_operandos.quitar()
    operador = pila_operadores.quitar()
    nuevo_operando = ""+operador+operando1+operando2
    pila_operandos.insertar(nuevo_operando)
           
expresion = pila_operandos.quitar()
print("La expresion en postfijo es: ", expresion)