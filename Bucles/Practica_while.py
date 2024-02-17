# # i=1

# # while i<=10:
# #     print("Ejecucion " + str(i))

# # print("Termino la ejecucion")
# #################################

# #edad=int(input("Introduce la edad: "))

# # while edad<0 or edad>100:
# #     print("Has introducido una edad incorrecta")
# #     edad=int(input("Introduce la edad: "))

# # print("PUEDES PASAR")
# # print("Tu edad es de " +str(edad))
# ######################################################

# import math

# print("Programa de calculo de raiz cuadrada")

# numero=int(input("Introduce un numero: "))
# intentos=0

# while numero<0:
#     print("no se puede obtener la raiz de un numero NEGATIVO")
#     if intentos==2:
#         print("Haz consumido demasiados intentos")
#         break;
#     numero=int(input("Introduce un numero: "))
#     if numero<0:
#         intentos=intentos+1

# if intentos <2:
#     solucion=math.sqrt(numero)
#     print("La raiz cuadrada de "+ str(numero) + " es " + str(solucion))
###############################################
# for letra in "Python":

#     if letra=="h":
#         continue
#     print ("Letra: " + letra)
##################################################
# nombre ="Raymundo Pichardo"
# contador=0
# for i in nombre:
#     if i == " ":
#         continue
#     contador+=1
# print(contador)
################################

email=input("Introduce tu email, por favor: ")

for i in email:
    if i =="@":
        arroba=True
        break;
else:
    arroba=False

print(arroba)