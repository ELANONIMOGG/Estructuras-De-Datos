from TDA_pila import Pila
import random

baraja = Pila()
numero = 10

def menu():
    print("1.- Nueva baraja")
    print("2.- Cortar ")
    print("3.- Mezclar ")
    print("4.- Mezclar en 3 ")
    print("5.- Imprimir ")
    print("6.- Salir ")

menu()
respuesta = int(input("Selecciona una opcion: "))

while respuesta != 6:
    match respuesta:
        case 1:
            baraja.reiniciar()
            for i in range(numero):
                baraja.insertar(i)
        case 2:
            pila1 = Pila()
            pila2 = Pila()
            mitad = numero // 2
            for i in range(mitad):
                pila1.insertar(baraja.quitar())
            while not baraja.pila_vacia():
                pila2.insertar(baraja.quitar())
            while not pila1.pila_vacia():
                baraja.insertar(pila1.quitar())
            while not pila2.pila_vacia():
                baraja.insertar(pila2.quitar())
            print("Baraja cortada.")
        case 3:
        # Mezclar la baraja
            pila1 = Pila()
            pila2 = Pila()
            mitad = numero // 2
            for i in range(mitad):
                pila1.insertar(baraja.quitar())
            while not baraja.pila_vacia():
                pila2.insertar(baraja.quitar())
            while not pila1.pila_vacia() or not pila2.pila_vacia():
                if not pila1.pila_vacia():
                    baraja.insertar(pila1.quitar())
                if not pila2.pila_vacia():
                    baraja.insertar(pila2.quitar())
            print("Baraja mezclada.")
        case 4:
        # Mezclar las cartas en montones de 3
            pila1 = Pila()
            pila2 = Pila()
            pila3 = Pila()
            tercio = numero // 3
            for i in range(tercio):
                pila1.insertar(baraja.quitar())
                pila2.insertar(baraja.quitar())
                pila3.insertar(baraja.quitar())
            while not pila1.pila_vacia() or not pila2.pila_vacia() or not pila3.pila_vacia():
                if not pila1.pila_vacia():
                    baraja.insertar(pila1.quitar())
                if not pila2.pila_vacia():
                    baraja.insertar(pila2.quitar())
                if not pila3.pila_vacia():
                    baraja.insertar(pila3.quitar())
            print("Baraja mezclada en tercios.")
        case 5:
            print(baraja.imprime())
        case _:
            print("error 404")    
    menu()
    respuesta = input("Selecciona una opcion: ")
