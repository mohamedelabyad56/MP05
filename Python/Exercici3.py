class ColaLIFO:

    def __init__(self):

        self.pila = []

    def agregar(self, elemento):

        self.pila.append(elemento)

    def extraer(self):

        if self.esta_vacia():
            raise IndexError("La pila está vacía. No se puede extraer elementos.")
        return self.pila.pop()

    def ver_ultimo(self):
      
        if self.esta_vacia():
            raise IndexError("La pila está vacía. No se puede ver elementos.")
        return self.pila[-1]

    def esta_vacia(self):
      
        return len(self.pila) == 0

    def longitud(self):

        return len(self.pila)

# Ejemplo de uso
if __name__ == "__main__":
    pila = ColaLIFO()
    # Agregar elementos a la pila
    pila.agregar("A")
    pila.agregar("B")
    pila.agregar("C")

    # Ver el último elemento
    print("Ultimo elemento:", pila.ver_ultimo())  # Salida: "C"

    # Extraer elementos de la pila
    print("Elemento extraido:", pila.extraer())   # Salida: "C"
    print("Ultimo elemento:", pila.ver_ultimo())  # Salida: "B"

    # Longitud de la pila
    print("Longitud de la pila:", pila.longitud())  # Salida: 2

    # Verificar si la pila está vacía
    print("La pila esta vacia?:", pila.esta_vacia())  # Salida: False

    # Extraer todos los elementos
    pila.extraer()
    pila.extraer()

    # Verificar nuevamente si la pila está vacía
    print("La pila esta vacia?:", pila.esta_vacia())  # Salida: True
