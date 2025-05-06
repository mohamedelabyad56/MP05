# Definición de clases

# Clase base: Projecte
class Projecte:
    def __init__(self, nom, duracio, llenguatge):
        self.nom = nom
        self.duracio = duracio
        self.llenguatge = llenguatge

    def mostrar_informacio(self):
        return f"Projecte: {self.nom}, Duració: {self.duracio} mesos, Llenguatge: {self.llenguatge}"

# Subclases: ProjecteIntern i ProjecteExtern
class ProjecteIntern(Projecte):
    def __init__(self, nom, duracio, llenguatge, responsable, departament):
        super().__init__(nom, duracio, llenguatge)
        self.responsable = responsable
        self.departament = departament

    def mostrar_informacio(self):
        base_info = super().mostrar_informacio()
        return f"{base_info}, Responsable: {self.responsable}, Departament: {self.departament}"

class ProjecteExtern(Projecte):
    def __init__(self, nom, duracio, llenguatge, client, pressupost):
        super().__init__(nom, duracio, llenguatge)
        self.client = client
        self.pressupost = pressupost

    def mostrar_informacio(self):
        base_info = super().mostrar_informacio()
        return f"{base_info}, Client: {self.client}, Pressupost: {self.pressupost}K€"

# Classe: Equip
class Equip:
    def __init__(self, nom_equip):
        self.nom_equip = nom_equip
        self.membres = []

    def afegir_membre(self, membre):
        self.membres.append(membre)

    def mostrar_informacio(self):
        return f"Equip: {self.nom_equip}, Membres: {len(self.membres)}"

    def mostrar_membres(self):
        return "\n".join([membre.mostrar_informacio() for membre in self.membres])

# Classe: Membre
class Membre:
    def __init__(self, nom, rol, experiencia):
        self.nom = nom
        self.rol = rol
        self.experiencia = experiencia

    def mostrar_informacio(self):
        return f"Membre: {self.nom}, Rol: {self.rol}, Experiència: {self.experiencia} anys"

# Classe: Tasca
class Tasca:
    def __init__(self, titol, estat, responsable):
        self.titol = titol
        self.estat = estat
        self.responsable = responsable

    def mostrar_informacio(self):
        return f"Tasca: {self.titol}, Estat: {self.estat}, Responsable: {self.responsable.nom}"

# Programa Principal
if __name__ == "__main__":
    # Crear un projecte intern
    projecte_intern = ProjecteIntern(
        nom="Aplicació CRM Interna",
        duracio=12,
        llenguatge="Python",
        responsable="Joan Rovira",
        departament="IT"
    )

    # Crear un projecte extern
    projecte_extern = ProjecteExtern(
        nom="Plataforma E-learning",
        duracio=18,
        llenguatge="Java",
        client="Educorp",
        pressupost=300
    )

    # Crear un equip i afegir membres
    equip = Equip("Equip Desenvolupament")
    membre1 = Membre("Anna", "Desenvolupadora", 3)
    membre2 = Membre("Marc", "Tester", 2)
    equip.afegir_membre(membre1)
    equip.afegir_membre(membre2)

    # Crear tasques i assignar-les
    tasca1 = Tasca("Definir requeriments", "pendent", membre1)
    tasca2 = Tasca("Provar funcionalitats", "pendent", membre2)

    # Mostrar informació
    print("Informació del projecte intern:")
    print(projecte_intern.mostrar_informacio())

    print("\nInformació de l'equip:")
    print(equip.mostrar_informacio())
    print(equip.mostrar_membres())

    print("\nInformació del projecte extern:")
    print(projecte_extern.mostrar_informacio())
