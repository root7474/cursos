# Ejercicio 6.1
# Autor: David Rodríguez

class Vehiculo:
    def __init__(self):
        self.__color = None
        self.__ruedas = None
        self.__puertas = None
    
    def setColor(self, color:str):
        self.__color = color
    
    def getColor(self):
        return self.__color
    
    def setRuedas(self, ruedas:int):
        self.__ruedas = ruedas
    
    def getRuedas(self):
        return self.__ruedas
    
    def setPuertas(self, puertas:int):
        if puertas == 2 or puertas == 4:
            self.__puertas = puertas
        
    def getPuertas(self):
        return self.__puertas
    
class Coche(Vehiculo):
    def __init__(self):
        super().__init__()
        self.__velocidad = None
        self.__Cilindrada = None
    
    def setVelocidad(self, velocidad):
        self.__velocidad = velocidad
    
    def getVelocidad(self):
        return self.__velocidad
    
    def setCilindrada(self, cilindrada):
        self.__Cilindrada = cilindrada
        
    def getCilindrada(self):
        return self.__Cilindrada
    
def main():
    coche = Coche()
    
    nombre = input("\nBienvenido... \nDigita tu nombre: ")
    color = input("\nDigita el color de tu vehículo: ")
    ruedas = 4
    puertas = int(input("Digita el número de puertas de tu vehículo (2 0 4): "))
    velocidad = eval(input("Digita la velocidad de tu vehículo (en Km/h): "))
    cilindrada = eval(input("Digita la cilindrada de tu vehículo (en cm³): "))
    
    coche.setColor(color)
    coche.setRuedas(ruedas)
    coche.setPuertas(puertas)
    coche.setVelocidad(velocidad)
    coche.setCilindrada(cilindrada)
    
    print(f"\n{nombre} tu vehículo es de color {coche.getColor()} con {coche.getRuedas()} ruedas, de {coche.getPuertas()} puertas, "
          f"con velocidad de {coche.getVelocidad()} Km/h y cilindrada de {coche.getCilindrada()} cm³\n")
    
main()
