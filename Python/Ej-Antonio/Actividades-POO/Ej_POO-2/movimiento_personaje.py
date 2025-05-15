def crear_mapa(filas, columnas):
    mapa = [['.' for _ in range(columnas)] for _ in range(filas)]
    return mapa

def mostrar_mapa(mapa, pos_x, pos_y):
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if i == pos_x and j == pos_y:
                print('P', end=' ')
            else:
                print(mapa[i][j], end=' ')
        print()

def mover_personaje(tecla, x, y, filas, columnas):
    if tecla == 'w' and x > 0:
        x -= 1
    elif tecla == 's' and x < filas - 1:
        x += 1
    elif tecla == 'a' and y > 0:
        y -= 1
    elif tecla == 'd' and y < columnas - 1:
        y += 1
    return x, y

# Inicializar
filas, columnas = 5, 5
mapa = crear_mapa(filas, columnas)
x, y = 2, 2  # posición inicial

# Juego
while True:
    mostrar_mapa(mapa, x, y)
    tecla = input("Mover (WASD, q para salir): ").lower()
    if tecla == 'q':
        break
    x, y = mover_personaje(tecla, x, y, filas, columnas)
