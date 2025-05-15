class Pregunta:
    def __init__(self, pregunta, opciones, respuesta_correcta):
        self.pregunta = pregunta
        self.opciones = opciones  # Lista de 4 opciones
        self.respuesta_correcta = respuesta_correcta

    def es_correcta(self, respuesta):
        return respuesta == self.respuesta_correcta

class JuegoTrivia:
    def __init__(self):
        self.preguntas = []
        self.puntuacion = 0

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def iniciar_juego(self):
        print("¡Bienvenido al Trivia de Grand Theft Auto!")
        for i, pregunta in enumerate(self.preguntas, 1):
            print(f"\nPregunta {i}: {pregunta.pregunta}")
            for j, opcion in enumerate(pregunta.opciones, 1):
                print(f"{j}. {opcion}")
            
            try:
                respuesta = int(input("Selecciona la opción correcta (1-4): ")) - 1
                if 0 <= respuesta < 4:
                    if pregunta.es_correcta(respuesta):
                        print("¡Correcto!")
                        self.puntuacion += 10
                    else:
                        print("Incorrecto. La respuesta correcta era:", pregunta.opciones[pregunta.respuesta_correcta])
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        print(f"\nJuego terminado. Puntuación final: {self.puntuacion}")

# Ejemplo de uso
if __name__ == "__main__":
    juego = JuegoTrivia()
    
    # Crear preguntas sobre GTA
    p1 = Pregunta(
        "¿En qué año se lanzó Grand Theft Auto V?",
        ["2011", "2012", "2013", "2014"],
        2  # Índice de la respuesta correcta
    )
    p2 = Pregunta(
        "¿Cuál es la ciudad principal en Grand Theft Auto: San Andreas?",
        ["Liberty City", "Vice City", "Los Santos", "Las Venturas"],
        2
    )
    p3 = Pregunta(
        "¿Cuál de estos personajes es un protagonista en GTA V?",
        ["Niko Bellic", "Michael De Santa", "CJ", "Tommy Vercetti"],
        1
    )
    p4 = Pregunta(
        "¿Qué compañía desarrolla la serie Grand Theft Auto?",
        ["Ubisoft", "Rockstar Games", "Electronic Arts", "Bethesda"],
        1
    )
    
    juego.agregar_pregunta(p1)
    juego.agregar_pregunta(p2)
    juego.agregar_pregunta(p3)
    juego.agregar_pregunta(p4)
    
    juego.iniciar_juego()