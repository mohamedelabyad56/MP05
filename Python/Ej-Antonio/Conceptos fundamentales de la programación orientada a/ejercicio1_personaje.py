

class Personaje:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

    def saludar(self):
        print(f"Hola, soy {self.nombre} y estoy en el nivel {self.nivel}.")


p1 = Personaje("Arthas", 10)
p2 = Personaje("Sylvanas", 12)

p1.saludar()
p2.saludar()
