

class Arma:
    durabilidad = 100  

    def __init__(self, nombre, daño, tipo):
        self.nombre = nombre
        self.daño = daño
        self.tipo = tipo


arma3 = Arma("Hacha", 45, "Cuerpo a cuerpo")
arma4 = Arma("Varita mágica", 20, "Mágica")

print(f"{arma3.nombre} - Durabilidad: {Arma.durabilidad}")
print(f"{arma4.nombre} - Durabilidad: {Arma.durabilidad}")
