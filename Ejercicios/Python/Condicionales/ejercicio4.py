##Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete
##mostrar un mensaje "Promocionado".
nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota:"))
suma = nota1+nota2+nota3
promedio=suma/3
if promedio >= 7:
    print(f"Promocionado, nota {promedio}")
else:
    print(f"Suspendido con una nota promedio de {promedio}")