a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
if b == 0:
 print("La división por cero no está definida.")
else:
 cociente = a / b
 print("El cociente de {} y {} es: {}".format(a, b, cociente))
