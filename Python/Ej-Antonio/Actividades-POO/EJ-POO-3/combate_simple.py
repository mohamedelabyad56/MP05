class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def atacar(self, enemigo):
        print(f"{self.nombre} ataca a {enemigo.nombre} causando {self.ataque} de daño.")
        enemigo.vida -= self.ataque

    def esta_vivo(self):
        return self.vida > 0

def combate(jugador, enemigo):
    turno = 1
    while jugador.esta_vivo() and enemigo.esta_vivo():
        print(f"\n--- Turno {turno} ---")
        jugador.atacar(enemigo)
        if enemigo.esta_vivo():
            enemigo.atacar(jugador)
        print(f"{jugador.nombre}: {jugador.vida} HP")
        print(f"{enemigo.nombre}: {enemigo.vida} HP")
        turno += 1

    if jugador.esta_vivo():
        print(f"\n{jugador.nombre} ha ganado el combate.")
    else:
        print(f"\n{enemigo.nombre} ha ganado el combate.")

# Ejemplo
jugador = Personaje("Héroe", 100, 20)
enemigo = Personaje("Orco", 80, 15)
combate(jugador, enemigo)
