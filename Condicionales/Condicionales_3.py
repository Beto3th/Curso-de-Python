salario_presidente=int(input("Introduce el salario del presidente: "))
print("Salario presidente: "+ str(salario_presidente) )

salario_director=int(input("Introduce el salario del director: "))
print("Salario director: "+ str(salario_director) )

salario_jefe=int(input("Introduce el salario del jefe: "))
print("Salario jefe: "+ str(salario_jefe) )

salario_admin=int(input("Introduce el salario del admin: "))
print("Salario admin: "+ str(salario_admin) )

if salario_admin<salario_jefe<salario_director<salario_director:
    print("Todo correcto")
else:
    print("algo esta mal")