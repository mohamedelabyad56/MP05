class Persona:
    def __init__(self, nom, edat, dni):
        self.__nom = nom  # Atribut privat
        self.__edat = edat  # Atribut privat
        self.__dni=dni
    
    # Mètode públic per accedir a l'atribut nom
    def obtenir_nom(self):
        return self.__nom
    
    # Mètode públic per modificar l'edat
    def canviar_edat(self, nova_edat):
        if nova_edat > 0:
            self.__edat = nova_edat
        else:
            print("L'edat ha de ser un valor positiu.")
    def cambiar_dni()
 
# Crear una instància de la classe Persona
persona1 = Persona("Anna", 25)
 
# Intentar accedir directament als atributs privats (això produirà un error)
# print(persona1.__nom)  # Això provocarà un error
 
# Utilitzem els mètodes públics per accedir i modificar les dades encapsulades
print(persona1.obtenir_nom())  # Anna
persona1.canviar_edat(30)
