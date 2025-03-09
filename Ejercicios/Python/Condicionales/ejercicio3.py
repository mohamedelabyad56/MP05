##Realizar un programa que solicite la carga por teclado de dos números,
##si el primero es mayor al segundo informar su suma y diferencia,
##en caso contrario informar el producto y la división
##del primero respecto al segundo.
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))
suma = num1+num2
div = num1/num2
mul = num1*num2
if num1 > num2:
    print(f"la suma es {suma} y la diferencia es {num1-num2} ")
elif num1<num2:
    print(f"el producto de los dos numeros es iggaul a {mul} y la divicion es {div}")
