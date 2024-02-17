# Crea un programa que pida números infinitamente. 
# Los números introducidos deben ser cada vez mayores 
# El programa finalizará cuando se introduce un número menor que el anterior.

print("WHILE: EJERCICIO 1")

num1 = int(input("Introduce el primer numero: "))
num2 = int (input("Introduce el segundo numero: "))

while num2>num1:
    num1=num2
    num2=int(input("Introduce otro numero mayor al anterior: "))
    

print("Programa finalizado")