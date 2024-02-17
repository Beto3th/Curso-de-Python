# Crea un programa que pida números positivos indefinidamente. 
# El programa termina cuando se introduce un número negativo. 
# Finalmente el programa muestras la suma de todos los números introducidos

print("Numeros positivos indefinidamente")

num1=int(input("Ingresa el primer numero: "))
res=0
#num2=int(input("Ingresa el segundo numero: "))

while num1 >= 0:
    res = res + num1
    num1=int(input("Ingresa otro numero positivo: "))

print("Ingresaste un numero negativo... La suma total es " + str(res))