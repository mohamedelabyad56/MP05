

class Arma:
    def __init__(self, nombre, daño, tipo):
        self.nombre = nombre
        self.daño = daño
        self.tipo = tipo

    def mostrar_info(self):
        return f"Arma: {self.nombre}, Daño: {self.daño}, Tipo: {self.tipo}"

    def usar(self):
        print("Usando el arma")

    def guardar(self):
        print("Guardando el arma")


arma2 = Arma("Arco largo", 25, "A distancia")
print(arma2.mostrar_info())
arma2.usar()
arma2.guardar()
