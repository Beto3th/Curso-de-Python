class Persona():

    def __init__(self, nombre, edad, LugarResidencia) :
        
        self.nombre=nombre
        self.edad=edad
        self.residencia=LugarResidencia

    def descripcion(self):

        print("Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ", self.residencia)

class Empleado(Persona):
    
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado) :

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario=salario
        self.antiguedad=antiguedad
    
    def descripcion(self):

        super().descripcion()

        print("Salario: ", self.salario, "Antigüedad: ", self.antiguedad, " years")


Raymundo = Empleado(1500, 10, "Raymundo", 25, "Fresnillo")

Raymundo.descripcion()

print(isinstance(Raymundo, Empleado))