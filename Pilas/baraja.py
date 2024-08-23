from TDA_pila import Pila
import random

baraja = Pila()
numero = 10
def menu():
    print("1.- Nueva baraja")
    print("2.- Cortar ")
    print("3.- Mezclar ")
    print("4.- Imprimir ")
    print("5.- Barajear de 3 ")
    print("6.- Salir ")

menu()
respuesta = input("Selecciona una opcion: ")
while respuesta != "5":
        if respuesta == "1":
            baraja.reiniciar()
            for i in range (numero):
               baraja.insertar(i)
        elif respuesta == "2":
            pila1 = Pila()
            pila2 = Pila()
            mitad = numero//2
            for i in range (mitad):
                pila1.insertar(baraja.quitar())
            while not baraja.pila_vacia():
                pila2.insertar(baraja.quitar)
            while not pila1.pila_vacia():
                baraja.insertar(pila1.quitar())
            while not pila2.pila_vacia():
                baraja.insertar(pila2.quitar())
        elif respuesta == "3":
            #mezclar la baraja
            
            for i in range (mitad):
                pila1.insertar(baraja.quitar())
            while not baraja.pila_vacia():
                pila2.insertar(baraja.quitar)
            while not pila1.pila_vacia() or not pila2.pila_vacia():
                if not pila1.pila_vacia():
                    baraja.insertar(pila1.quitar)
                if not pila2.pila_vacia():
                    baraja.insertar(pila2.quitar)
            
            print("Cartas mezcladas")
        elif respuesta == "4":
            #Mezclar las cartas en montones de 3
            pila1 = Pila()
            pila2 = Pila()
            pila3 = Pila()
            mitad = numero//3
            

            for i in range (mitad):
                pila1.insertar(baraja.quitar())
            while not baraja.pila_vacia():
                pila2.insertar(baraja.quitar)
                pila3.insertar(baraja.quitar)
            while not pila1.pila_vacia() or not pila2.pila_vacia() or pila3.pila_vacia:
                if not pila1.pila_vacia():
                    baraja.insertar(pila1.quitar)
                if not pila2.pila_vacia():
                    baraja.insertar(pila2.quitar)
                if not pila3.pila_vacia():
                    baraja.insertar(pila2.quitar)
            print("Baraja En 3")



        elif respuesta == "5":
            print(baraja.imprime())
        
        menu()
        respuesta = input("Selecciona una opcion: ")
        
                