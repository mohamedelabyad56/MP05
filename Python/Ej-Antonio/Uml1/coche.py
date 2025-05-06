class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
    
    def encender(self):
        return f"Motor {self.tipo} de {self.potencia} HP encendido."

class Coche:
    def __init__(self, marca, modelo, año, tipo_motor, potencia_motor):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.motor = Motor(tipo_motor, potencia_motor)
    
    def arrancar(self):
        return f"{self.marca} {self.modelo} arrancando con {self.motor.encender()}"
    
    def detener(self):
        return f"{self.marca} {self.modelo} detenido."