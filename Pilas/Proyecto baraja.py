# Importar la implementación de la cola lineal desde el archivo donde está definiO, import Cola_Lin
# Función para simular la atención en un banco utilizando una cola de clientes
def simulacion_banco():
    # Crear una cola para manejar la llegada de clientes
    cola_clientes = Cola_Lineal()

    # Llegada de clientes
    cola_clientes.insertar("Cliente 1")
    cola_clientes.insertar("Cliente 2")
    cola_clientes.insertar("Cliente 3")
    cola_clientes.insertar("Cliente 4")
    cola_clientes.insertar("Cliente 5")

    # Atención de clientes
    print("Inicio de la simulación de atención en el banco:")

    while not cola_clientes.cola_vacia():
        # El próximo cliente en la cola es atendido
        cliente_actual = cola_clientes.quitar()
        print(f"Atendiendo a {cliente_actual}")

    print("Fin de la simulación.")

# Ejecutar la simulación del banco
simulacion_banco()
