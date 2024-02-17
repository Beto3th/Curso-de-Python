print("CORREO ELECTRONICO")

counter_1=0
counter_2=0

email=input("Ingrese su correo electronico: ")

for i in range(len(email)):
    if email[i]==".":
        counter_1=1
    if email[i]=="@":
        counter_2=1

if counter_1 == 0 or counter_2==0:
    print("emal erroneo")
else:
    print("Email Correcto")