from abc import ABC, abstractmethod


class Interruptor(ABC):
    @abstractmethod
    def encendido(self):
        pass

    @abstractmethod
    def apagado(self):
        pass


class Bombilla(Interruptor):
    def encendido(self):
        print("Bombilla: encendida...")

    def apagado(self):
        print("Bombilla: apagada...")


class Led_Fan(Interruptor):
    def encendido(self):
        print("Led (Fan): encendido...")

    def apagado(self):
        print("Led (Fan): apagado...")


class Interruptor_electrico:

    def __init__(self, c: Interruptor):
        self.cliente = c
        self.encendido = False

    def aplicacion(self):
        if self.encendido:
            self.cliente.apagado()
            self.encendido = False
        else:
            self.cliente.encendido()
            self.encendido = True


B = Bombilla()
F = Led_Fan()
switch = Interruptor_electrico(F)
switch.aplicacion()
switch.aplicacion()
switch = Interruptor_electrico(B)
switch.aplicacion()
switch.aplicacion()
