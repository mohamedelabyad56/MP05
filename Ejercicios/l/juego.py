#importar random
import random

#en la linea de abajo he declarado una variable para generar un numero aleatorio entre el 1-100
numAleatorio = random.randint(1, 100)

#en la linea de abajo he declardo el una variable para controlar el numero de intentos
veces = 10
#Este bucle sirve para preguntarle al usuario hasta que se agote el
#número de intentos o hasta que el usuario adivine el número.
for intento in range(veces):
    valor = int(input("Ingresa un número entre 1 y 100: "))

    if valor == numAleatorio:
        print(f"¡Has ganado! El número {valor} es correcto.")
        break
    elif valor < numAleatorio:
        print(f"El número {valor} es menor.")
    else:
        print(f"El número {valor} es mayor.")

# este if imprime un mensaje si el usuario no logra adivinar el numero
if valor != numAleatorio:
    print(f"Has perdido. El número correcto era {numAleatorio}.")
