def presentacio():
    print("Programa que permite cargar dos valores por teclado.")
    print("Efectua la suma de los valores")
    print("Muestra el resultado de la suma")
    print("*********************************")
def carga_suma():
    cr1= int(input("Ingresa el primer numero: "))
    cr2= int(input("Ingresa el primer numero: "))
    suma = cr1+cr2
    print(f"La suma es igual a {suma}")
def finalizacion():
    print("***********************************")
    print("Gracias por utilizar este programa")

presentacio()
carga_suma()
for x in range(4):
    if x == -1:
        break;
    carga_suma()
finalizacion()
