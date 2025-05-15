import json

class Personaje:
    def __init__(self, nombre, nivel=1, experiencia=0, inventario=None):
        self.nombre = nombre
        self.nivel = nivel
        self.experiencia = experiencia
        self.inventario = inventario if inventario is not None else []

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "nivel": self.nivel,
            "experiencia": self.experiencia,
            "inventario": self.inventario
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            nombre=data["nombre"],
            nivel=data["nivel"],
            experiencia=data["experiencia"],
            inventario=data["inventario"]
        )

    def guardar(self, archivo):
        try:
            with open(archivo, 'w') as f:
                json.dump(self.to_dict(), f, indent=4)
            print(f"Personaje {self.nombre} guardado exitosamente.")
        except Exception as e:
            print(f"Error al guardar: {e}")

    @classmethod
    def cargar(cls, archivo):
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
            return cls.from_dict(data)
        except FileNotFoundError:
            print(f"El archivo {archivo} no existe.")
            return None
        except Exception as e:
            print(f"Error al cargar: {e}")
            return None

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un personaje
    heroe = Personaje("Aragorn", 5, 250, ["Espada", "Poción"])
    
    # Guardar personaje
    heroe.guardar("personaje.json")
    
    # Cargar personaje
    personaje_cargado = Personaje.cargar("personaje.json")
    if personaje_cargado:
        print(f"Personaje cargado: {personaje_cargado.nombre}, Nivel: {personaje_cargado.nivel}")
        print(f"Inventario: {personaje_cargado.inventario}")