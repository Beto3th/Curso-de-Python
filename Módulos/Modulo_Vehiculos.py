class Vehiculos():#Clase Padre

    def __init__(self, marca, modelo): #Declaracion de variables
        
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self): #Metodos

        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True
    
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", 
            self.acelera, "\nFrenando: ", self.frena)

class Moto(Vehiculos): #Clase a la que se hereda
    hcaballito=""
    
    def caballito(self):
        self.hcaballito="Esta haciendo el caballito"
    
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", 
            self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)

class Furgoneta(Vehiculos):#Nueva clase hereditaria
    
    def carga(self, cargar):
        self.cargado=cargar

        if (self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


class Electricos(Vehiculos):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia=100
    
    def cargarEnergia(self):
        self.cargando=True

class BiciElectrica(Electricos,Vehiculos):
    pass

