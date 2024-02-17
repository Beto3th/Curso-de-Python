# def generarPares(limite):
#     num=1

#     miLista =[]

#     while num < limite:
#         miLista.append(num*2)

#         num=num+1
#     return miLista

# print(generarPares(10))
###########################
def generarPares(limite):
    num=1

    while num < limite:
        yield num*2
        num=num+1

devuelvePares=generarPares(10)


print(next(devuelvePares))

print("Código....")
print(next(devuelvePares))

print("Código....")
print(next(devuelvePares))

print("Código....")
print(next(devuelvePares))