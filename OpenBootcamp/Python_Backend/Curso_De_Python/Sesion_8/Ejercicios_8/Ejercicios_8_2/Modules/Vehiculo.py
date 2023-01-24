class Vehiculo:
    def __init__(self):
        self.__tipo = None
        self.__marca = None
        self.__color = None
        self.__motor = None
        self.__ventanas = 0
        self.__puertas = 0
        
    def setTipo(self, tipo):
        self.__tipo = tipo
        
    def getTipo(self):
        return self.__tipo
        
    def setMarca(self, marca):
        self.__marca = marca
        
    def getMarca(self):
        return self.__marca
    
    def setColor(self, color):
        self.__color = color
        
    def getColor(self):
        return self.__color
    
    def setMotor(self, motor):
        self.__motor = motor
        
    def getMotor(self):
        return self.__motor
    
    def setVentanas(self, ventanas):
        self.__ventanas = ventanas
        
    def getVentanas(self):
        return self.__ventanas
    
    def setPuertas(self, puertas):
        self.__puertas = puertas
        
    def getPuertas(self):
        return self.__puertas
