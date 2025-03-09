##Realizar la carga del precio de un producto y la cantidad a llevar.
##Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio del producto)
cantidad= int(input("intruduzca la cantidad de los productos: "))
precio= int(input("Introduce el precio de los productos: "))

apagar = precio*cantidad
print(f"la cantidad de los productos es {cantidad} y vale {precio}€ por pieza en total son {apagar}€")