# Composición
from urllib.request import CacheFTPHandler

class Motor:
    tipo = "Diesel"

class Ventanas:
    cantidad = 5
    
    def cambiarCantidad(self, valor):
        self.cantidad = valor

class Ruedas:
    cantidad = 4

class Carroceria:
    ventanas = Ventanas()
    ruedas = Ruedas()

class Coche:
    motor = Motor()
    carroceria = Carroceria()

def main():
    c = Coche()
    print("Motor es:", c.motor.tipo)
    print("Ventanas:", c.carroceria.ventanas.cantidad)
    
    c.carroceria.ventanas.cambiarCantidad(6)
    print("\nVentanas:", c.carroceria.ventanas.cantidad)
    
main()
