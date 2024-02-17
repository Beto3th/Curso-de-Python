# Crea un programa que pida introducir una dirección de email por teclado.
# El programa debe imprimir en consola si la dirección de email es correcta
# o no en función de si esta tiene el símbolo ‘@’. Si tiene una ‘@’ la dirección
# será correcta. Si tiene más de una o ninguna ‘@’ la dirección será errónea. 
# Si la ‘@’ está al comienzo de la dirección de email o al final, la dirección también será errónea,

email=input("Introduzca su email => ")
contador=0
for i in range(len(email)):
    if (email[i]=="@" and email[0]!="@"):
        contador=+1
        if contador==1:
            print("La direccion de email es correcta")
        else:
            print("La direccion de correo NO es correcta")
    