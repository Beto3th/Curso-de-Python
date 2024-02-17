edad=input("Introduce tu edad: ")

while (edad.isdigit()==False):
    print("Porfavor introduce un valor numerico")
    edad=input("Introduce tu edad: ")

if (int(edad)<18):
    print("No puede pasar")
else:
    print("Puede pasar")