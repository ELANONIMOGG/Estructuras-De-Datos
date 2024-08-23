from TDA_pila import Pila

def paréntesis_balanceados(expresion):
    pilaaux = Pila()

    for caracter in expresion:
        if caracter == "(":
            pilaaux.insertar(caracter)
        elif caracter == ")":
            if pilaaux.pila_vacia():
                return False 
            pilaaux.quitar()
            
    return not pilaaux.pila_vacia()  

def es_operador(caracter):
    return caracter in ["^", "*", "/", "+", "-"]

def prioridad(caracter):
    if caracter == "^":
        return 3
    elif caracter in ["*", "/"]:
        return 2
    elif caracter in ["+", "-"]:
        return 1
    else:
        return 0

cadena = input("Expresion: ")

if paréntesis_balanceados(cadena):
    expresion_salida = ""
    pila_operadores = Pila()
    ultimo_caracter = None

    for caracter in cadena:
        if caracter.isdigit() or caracter.isalpha():  
            expresion_salida += caracter
        elif caracter == "(":
            if ultimo_caracter and (ultimo_caracter.isdigit() or ultimo_caracter.isalpha()):  
                print("Error: Falta un operador entre un número y un paréntesis.")
                exit()
            pila_operadores.insertar(caracter)    
        elif caracter == ")":
            while not pila_operadores.pila_vacia() and pila_operadores.tope_pila != "(":
                operador = pila_operadores.quitar()
                expresion_salida += operador
            if pila_operadores.tope_pila == "(":
                pila_operadores.quitar()  
        elif es_operador(caracter):
            while not pila_operadores.pila_vacia() and prioridad(caracter) <= prioridad(pila_operadores.tope_pila):
                operador = pila_operadores.quitar()
                expresion_salida += operador
            pila_operadores.insertar(caracter)
        else:
            print("Error: Carácter inválido encontrado:", caracter)
            exit()
        ultimo_caracter = caracter

    while not pila_operadores.pila_vacia():
        operador = pila_operadores.quitar()
        expresion_salida += operador    

    print("La expresion en postfijo es: ", expresion_salida)

else:
    print("Error: Los paréntesis no están puestos correctamente.")
