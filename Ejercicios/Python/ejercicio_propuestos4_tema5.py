##Calcular el sueldo mensual de un operario conociendo la cantidad de horas
##trabajadas y el valor por hora.
horas= int(input("Cuantas horas ha trabajado el operario: "))
precioH= int(input("Cuanto le pagan al operario por hora: "))
salario= precioH*horas
print(f"El operario ha trabajdo {horas}h y cobra {precioH}€ por hora, en total es {salario}€")

