def agregar_libro(biblioteca):
    try:
        id_libro = int(input("Introduce el ID del libro: "))
        if id_libro in biblioteca:
            print("El ID ya existe. Intenta con otro.")
            return
        titulo = input("Introduce el título del libro: ").strip()
        autor = input("Introduce el autor del libro: ").strip()
        cantidad = int(input("Introduce la cantidad de ejemplares disponibles: "))
        biblioteca[id_libro] = {"titulo": titulo, "autor": autor, "cantidad": cantidad}
        print("Libro añadido con éxito.")
    except ValueError:
        print("Error: Introduce valores válidos.")

def buscar_libro(biblioteca):
    try:
        id_libro = int(input("Introduce el ID del libro: "))
        if id_libro in biblioteca:
            libro = biblioteca[id_libro]
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Cantidad: {libro['cantidad']}")
        else:
            print("No se encontró un libro con ese ID.")
    except ValueError:
        print("Error: Introduce un número válido.")

def mostrar_todos_libros(biblioteca):

    if biblioteca:
        print("\nLibros disponibles:")
        for id_libro, info in biblioteca.items():
            print(f"ID: {id_libro}, Título: {info['titulo']}, Autor: {info['autor']}, Cantidad: {info['cantidad']}")
    else:
        print("La biblioteca está vacía.")

def prestar_libro(biblioteca):

    try:
        id_libro = int(input("Introduce el ID del libro: "))
        if id_libro in biblioteca:
            if biblioteca[id_libro]["cantidad"] > 0:
                biblioteca[id_libro]["cantidad"] -= 1
                print("Préstamo realizado con éxito.")
            else:
                print("No hay ejemplares disponibles para préstamo.")
        else:
            print("No se encontró un libro con ese ID.")
    except ValueError:
        print("Error: Introduce un número válido.")

def menu_biblioteca():

    biblioteca = {
        1: {"titulo": "Python para todos", "autor": "John Doe", "cantidad": 3},
        2: {"titulo": "Estructuras de Datos", "autor": "Anna Smith", "cantidad": 5},
        3: {"titulo": "Introducción a OOP", "autor": "Juan Costa", "cantidad": 2},
    }

    while True:
        print("\n--- MENÚ BIBLIOTECA ---")
        print("1. Añadir un nuevo libro")
        print("2. Buscar un libro")
        print("3. Mostrar todos los libros")
        print("4. Préstamo de un libro")
        print("5. Salir")

        try:
            opcion = int(input("Introduce una opción: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        if opcion == 1:
            agregar_libro(biblioteca)
        elif opcion == 2:
            buscar_libro(biblioteca)
        elif opcion == 3:
            mostrar_todos_libros(biblioteca)
        elif opcion == 4:
            prestar_libro(biblioteca)
        elif opcion == 5:
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    menu_biblioteca()