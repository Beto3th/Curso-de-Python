'''distancia>40km
numero hermanos > 2 
salario familiar <= 20000'''

print("PROGRAMA DE BECAS")

distancia = int(input("Introduce la distancia a la escuela en KM: "))
print(distancia)

numeroHermanos=int(input("Introduce el numero de hermanos: "))
print(numeroHermanos)

salarioFamiliar=int(input("Introduce el salario anual bruto: "))
print(salarioFamiliar)

if distancia>40 and numeroHermanos>2 or salarioFamiliar<=20000:
    print("Tienes derecho a beca")
else:
    print("no tienes derecho a beca") 