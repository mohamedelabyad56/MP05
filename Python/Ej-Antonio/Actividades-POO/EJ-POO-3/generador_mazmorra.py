import random

def generar_mazmorra(filas, columnas):
    mazmorra = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            if random.random() < 0.2:
                fila.append('#')  # pared
            else:
                fila.append('.')  # espacio vacío
        mazmorra.append(fila)

    # Colocar jugador en posición válida
    while True:
        x, y = random.randint(0, filas-1), random.randint(0, columnas-1)
        if mazmorra[x][y] == '.':
            mazmorra[x][y] = 'P'
            break

    return mazmorra

def mostrar_mazmorra(mazmorra):
    for fila in mazmorra:
        print(' '.join(fila))

# Uso
mazmorra = generar_mazmorra(10, 10)
mostrar_mazmorra(mazmorra)
