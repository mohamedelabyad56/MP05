

class Arma:
    def __init__(self, nombre, daño, tipo):
        self.nombre = nombre
        self.daño = daño
        self.tipo = tipo

    def mostrar_info(self):
        return f"Arma: {self.nombre}, Daño: {self.daño}, Tipo: {self.tipo}"


arma1 = Arma("Espada de fuego", 35, "Cuerpo a cuerpo")
print(arma1.mostrar_info())
