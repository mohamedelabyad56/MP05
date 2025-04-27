class Personaje:
    def __init__(self, nombre, vida=100, ataque=10):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def esta_vivo(self):
        return self.vida > 0

    def recibir_dano(self, dano):
        self.vida = max(0, self.vida - dano)
        print(f"{self.nombre} recibe {dano} de daño. Vida restante: {self.vida}")

    def atacar(self, enemigo):
        print(f"{self.nombre} ataca a {enemigo.nombre}")
        enemigo.recibir_dano(self.ataque)

class Guerrero(Personaje):
    def habilidad_especial(self, enemigo):
        dano = self.ataque * 2
        print(f"{self.nombre} usa Golpe Poderoso!")
        enemigo.recibir_dano(dano)

class Mago(Personaje):
    def habilidad_especial(self, enemigo):
        dano = self.ataque * 1.5
        print(f"{self.nombre} lanza Bola de Fuego!")
        enemigo.recibir_dano(dano)

class Arquero(Personaje):
    def habilidad_especial(self, enemigo):
        dano = self.ataque * 1.8
        print(f"{self.nombre} dispara Flecha Precisa!")
        enemigo.recibir_dano(dano)

def combate_por_turnos(jugador, enemigo):
    print(f"\n¡Combate iniciado: {jugador.nombre} vs {enemigo.nombre}!\n")
    
    while jugador.esta_vivo() and enemigo.esta_vivo():
        print(f"Vida de {jugador.nombre}: {jugador.vida}")
        print(f"Vida de {enemigo.nombre}: {enemigo.vida}")
        print("\nOpciones:")
        print("1. Ataque normal")
        print("2. Habilidad especial")
        
        try:
            opcion = int(input("Elige una acción (1-2): "))
            if opcion == 1:
                jugador.atacar(enemigo)
            elif opcion == 2:
                jugador.habilidad_especial(enemigo)
            else:
                print("Opción inválida.")
                continue
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if enemigo.esta_vivo():
            enemigo.atacar(jugador)

    if jugador.esta_vivo():
        print(f"\n¡{jugador.nombre} ha ganado el combate!")
    else:
        print(f"\n{enemigo.nombre} ha ganado el combate!")

# Ejemplo de uso
if __name__ == "__main__":
    guerrero = Guerrero("Conan", 150, 20)
    mago = Mago("Gandalf", 100, 15)
    
    combate_por_turnos(guerrero, mago)