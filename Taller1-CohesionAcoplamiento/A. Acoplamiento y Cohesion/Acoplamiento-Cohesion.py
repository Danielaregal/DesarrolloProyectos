import string
import random

class InformacionVehiculo:

    Marca: str
    Precio_Catalogo:int
    Electrico: bool
    
    def __init__(self, marca, electrico, precio_catalogo):
        self.Marca = marca
        self.Electrico = electrico
        self.Precio_Catalogo = precio_catalogo

    def impuestos(self):
        Porcentaje_Impuestos = 0.05
        if self.Electrico:
            Porcentaje_Impuestos = 0.02
        return Porcentaje_Impuestos * self.Precio_Catalogo

    def print(self):
        print(f"Marca: {self.Marca}")
        print(f"Impuesto a pagar: {self.impuestos()}")

class Vehiculo:

    Identificacion: str
    Placa: str
    Informacion: InformacionVehiculo

    def __init__(self, identificacion, placa, informacion):
        self.Identificacion = identificacion
        self.Placa = placa
        self.Informacion = informacion

    def print(self):
        print(f"Identificación: {self.Identificacion}")
        print(f"Placa: {self.Placa}")
        self.Informacion.print()


class Registro_Vehiculo:

    Informacion_Vehiculo = {}

    def adicion_informacion_vehiculo(self, marca, electrico, precio_catalogo):
        self.Informacion_Vehiculo[marca] = InformacionVehiculo(marca, electrico, precio_catalogo)

    def __init__(self):
        self.Informacion_Vehiculo = { }
        self.adicion_informacion_vehiculo("Tesla Modelo 3", True, 60000)
        self.adicion_informacion_vehiculo("Volkswagen ID3", True, 35000)
        self.adicion_informacion_vehiculo("BMW 5", False, 45000)
        self.adicion_informacion_vehiculo("Tesla Modelo Y", True, 75000)
   
    def generacion_identificacion_vehiculo(self, Longitud):
        return ''.join(random.choices(string.ascii_uppercase, k=Longitud))

    def generacion_placa(self, identificacion):
        return f"{identificacion[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def creacion_vehiculo(self, marca):
        Identificacion_vehiculo = self.generacion_identificacion_vehiculo(12)
        Placa_vehiculo = self.generacion_placa(Identificacion_vehiculo)
        return Vehiculo(Identificacion_vehiculo, Placa_vehiculo, self.Informacion_Vehiculo[marca])


class Aplicacion:

    def registro_vehiculo(self, marca: string):
        # create a registry instance
        Registro = Registro_Vehiculo()

        Vehiculo = Registro.creacion_vehiculo(marca)

        # print out the vehicle information
        Vehiculo.print()

app = Aplicacion()
app.registro_vehiculo("Volkswagen ID3")
app.registro_vehiculo("BMW 5")