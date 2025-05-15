class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def atacar(self, otro):
        daño = self.ataque - otro.defensa
        daño = max(daño, 0)
        otro.vida -= daño
        print(f"{self.nombre} ataca a {otro.nombre} causando {daño} de daño.")

    def esta_vivo(self):
        return self.vida > 0

# Crear personajes
p1 = Personaje("Guerrero", 100, 20, 5)
p2 = Personaje("Bestia", 80, 15, 3)

# Simular batalla
while p1.esta_vivo() and p2.esta_vivo():
    p1.atacar(p2)
    if p2.esta_vivo():
        p2.atacar(p1)

print(f"\nGanador: {p1.nombre if p1.esta_vivo() else p2.nombre}")
