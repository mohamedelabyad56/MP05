def calcular_coste_total(pedidos, cliente):
    """
    Calcula el coste total de todos los pedidos de un cliente.
    """
    if cliente in pedidos:
        total = sum(cantidad * precio_unitario for _, cantidad, precio_unitario in pedidos[cliente])
        return total
    else:
        return None

def clientes_pedidos_grandes(pedidos, limite=100):
    """
    Devuelve una lista de clientes con pedidos superiores al límite especificado.
    """
    return [cliente for cliente, articulos in pedidos.items() if sum(cantidad * precio_unitario for _, cantidad, precio_unitario in articulos) > limite]

def mostrar_pedidos_cliente(pedidos, cliente):
    """
    Muestra todos los pedidos detallados de un cliente.
    """
    if cliente in pedidos:
        for nombre_producto, cantidad, precio_unitario in pedidos[cliente]:
            print(f"Producto: {nombre_producto}, Cantidad: {cantidad}, Precio Unitario: {precio_unitario:.2f}")
    else:
        print(f"El cliente {cliente} no tiene pedidos registrados.")

def menu():
    """
    Muestra el menú interactivo para gestionar los pedidos de la tienda.
    """
    pedidos = {
        "Ana": [("Libro", 2, 10.0), ("Bolígrafo", 5, 1.5)],
        "Juan": [("Carpeta", 3, 4.5)],
        "Marta": [("Ordenador", 1, 800.0), ("Ratón", 2, 20.0)]
    }

    while True:
        print("\n--- MENÚ ---")
        print("1. Coste total de cada cliente")
        print("2. Clientes con pedidos superiores a 100 euros")
        print("3. Mostrar pedidos de un cliente")
        print("4. Salir")

        try:
            opcion = int(input("Introduce una opción: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        if opcion == 1:
            for cliente in pedidos:
                total = calcular_coste_total(pedidos, cliente)
                print(f"Cliente: {cliente}, Coste Total: {total:.2f} euros")

        elif opcion == 2:
            clientes = clientes_pedidos_grandes(pedidos)
            print("Clientes con pedidos superiores a 100 euros:")
            for cliente in clientes:
                print(f"- {cliente}")

        elif opcion == 3:
            cliente = input("Introduce el nombre del cliente: ").strip()
            print(f"Pedidos de {cliente}:")
            mostrar_pedidos_cliente(pedidos, cliente)

        elif opcion == 4:
            print("Saliendo del programa, Hasta pronto")
            break

        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    menu()
