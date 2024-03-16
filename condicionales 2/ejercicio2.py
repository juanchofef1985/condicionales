num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
if num1 > num2:
 print("El primer número ({}) es mayor que el segundo número ({}).".format(num1, num2))
 print("El segundo número ({}) es menor que el primer número ({}).".format(num2, num1))
elif num1 < num2:
 print("El segundo número ({}) es mayor que el primer número ({}).".format(num2, num1))
 print("El primer número ({}) es menor que el segundo número ({}).".format(num1, num2))
else:
 print("Ambos números son iguales.")
