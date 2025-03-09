##Ingresar el sueldo de una persona, si supera los 3000 dolares mostrar un
##mensaje en pantalla indicando que debe abonar impuestos.
num=int(input("cuanto ganas al mes: "))
sal=3000
if num > sal:
    print("tines que pagar impestos")
else:
    print("no tienes que pagar impuestos")