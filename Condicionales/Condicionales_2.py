print("FILTRO DE EDAD")

edadPersona=input("Ingrese su edad: ")#Variable de ka edad

def calcular(edad):#Funcion con el parametro esperado
    if edad<18:#Primera condicion
        print("NO puedes pasar")
    elif edad>95:#Segunda condicion
        print("Edad incorrecta")
    else:#Tercera condicion
        print("puedes pasar")       
print(calcular(int(edadPersona)))#Imprimir dependiendo de la condicion

print("PROGRAMA FINALIZADO")#Fin del programa