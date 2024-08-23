"""
IMPLEMENTAR UNA FUNCION PARA CALCULAR LA PONTENCIA DADO DOS NUMEROS ENTEROS, EL PRIMERO LA BASE Y EL 
SEGUNDO EL EXPONENTE


"""

def calcular_potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

potencia = calcular_potencia(base, exponente)
print(f"El resultado de elevar {base} a la potencia {exponente} es: {potencia}")