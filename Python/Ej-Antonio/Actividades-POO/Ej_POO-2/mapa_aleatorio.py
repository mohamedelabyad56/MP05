import random

def generar_mapa(filas, columnas):
    mapa = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            celda = random.choice(['.', '#'])
            fila.append(celda)
        mapa.append(fila)

    # Colocar al personaje en una posición aleatoria
    x, y = random.randint(0, filas - 1), random.randint(0, columnas - 1)
    mapa[x][y] = 'P'

    return mapa

def mostrar_mapa(mapa):
    for fila in mapa:
        print(' '.join(fila))

# Uso
mapa = generar_mapa(10, 10)
mostrar_mapa(mapa)
