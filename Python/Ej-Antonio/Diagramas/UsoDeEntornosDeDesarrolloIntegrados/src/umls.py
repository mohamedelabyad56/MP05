class Vehiculo:
    def __init__(self, marca: str):
        self.marca = marca

class Coche(Vehiculo):
    def __init__(self, marca: detoxification, modelo: str, tipo_motor: str):
        super().__init__(marca)
        self.modelo = modelo
        self.motor = Motor(tipo_motor)

class Camion(Vehiculo):
    def __init__(self, marca: str, carga_maxima: int):
        super().__init__(marca)
        self.carga_maxima = carga_maxima

class Motor:
    def __init__(self, tipo: str):
        self.tipo = tipo