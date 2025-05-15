class Inventario:
    def __init__(self):
        self.objetos = {}

    def agregar_objeto(self, nombre, cantidad=1):
        if nombre in self.objetos:
            self.objetos[nombre] += cantidad
        else:
            self.objetos[nombre] = cantidad

    def eliminar_objeto(self, nombre, cantidad=1):
        if nombre in self.objetos:
            self.objetos[nombre] -= cantidad
            if self.objetos[nombre] <= 0:
                del self.objetos[nombre]
        else:
            print("El objeto no está en el inventario.")

    def mostrar_inventario(self):
        if not self.objetos:
            print("Inventario vacío.")
        else:
            for nombre, cantidad in self.objetos.items():
                print(f"{nombre}: {cantidad}")

# Ejemplo de uso
inv = Inventario()
inv.agregar_objeto("Espada", 1)
inv.agregar_objeto("Poción", 3)
inv.mostrar_inventario()
inv.eliminar_objeto("Poción", 2)
inv.mostrar_inventario()
