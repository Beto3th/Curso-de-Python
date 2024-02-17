print("CONTRASEÑA")
contador=0
password=input("Ingresa tu contraseña: ")

for i in range(len(password)):
    if password[i]==" ":
        contador=1

if len(password) > 8 or contador>0:
    print("Contraseña erronea")
else:
    print("Contraseña OK")