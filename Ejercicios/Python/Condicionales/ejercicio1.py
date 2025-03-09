##Realizar un programa que solicite ingresar
##dos números distintos y muestre por pantalla el mayor de ellos.
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 >  num2:
    print(f"El número {num1} es mayor que el número {num2}")
elif num1 < num2:
        print(f"El número {num2} es mayor que el número {num1}")
else:
     print("los numero son iguales")
    