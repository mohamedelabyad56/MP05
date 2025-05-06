class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hablar(self):
        return f"{self.nombre} está hablando."
    
    def caminar(self):
        return f"{self.nombre} está caminando."

class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula
    
    def estudiar(self):
        return f"{self.nombre} con matrícula {self.matricula} está estudiando."