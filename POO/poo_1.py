class Coche():

    def __init__(self): #Inicializar variables
        self.__largoChasis=250 #Encapsulada (solo se puede acceder dentro de la clase)
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False
    
    def arrancar(self,arrancamos): #Metodo para arrancar el auto
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "EL coche esta en marcha "
        elif(self.__enmarcha and chequeo==False):
            return "Hay error en el chequeo"
    
        else:
            return "El coche esta parado"
        
    def estado(self): #MEtodo que imprime el estado del auto
        print("El coche tiene ",self.__ruedas," ruedas. Un ancho de ", self.__anchoChasis, 
            "y un  largo de ", self.__largoChasis)
    
    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False
        
miCoche=Coche() #Creacion del primer auto

print(miCoche.arrancar(True))
miCoche.estado()


print("------------------A continuacion creamos el segundo objeto------------------")

miCoche2=Coche() #Creacion del segundo auto 
print(miCoche2.arrancar(False))
miCoche2.estado()
