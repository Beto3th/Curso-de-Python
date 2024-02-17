class Coche():

    def desplazamiento(self):
        print("Me DESPLAZO UTILIZANDO CUATRO RUEDAS")


class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Moto()
desplazamientoVehiculo(miVehiculo)