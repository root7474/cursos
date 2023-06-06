# Tarea: Clase vehículo
# Autor: David Rodríguez

# Creamos una clase llamada "Vehiculo()"
class Vehiculo():
    __marca = None # Creamos un atributo privado "__marca" y lo inicializamos en None
    __color = None # Creamos un atributo privado "__color" y lo inicializamos en None
    
    # Creamos el constructor de la clase y le pasamos los parámetros de self, marca y color
    def __init__(self, marca, color):
        self.__marca = marca # Al atributo "__marca", le pasamos el valor del parámetro "marca"
        self.__color = color # Al atributo "__color", le pasamos el valor del parámetro "color"
    
    # Creamos los métodos get para cada uno de los atributos de esta clase
    def getMarca(self):
        return self.__marca # Retornamos el valor de "__marca"
    
    def getColor(self):
        return self.__color # Retornamos el valor de "__color"

# Creamos una clase llamada "Coche()" que hereda de la clase "Vehiculo()"
class Coche(Vehiculo):
    __potencia = 0 # Creamos un atributo privado "__potencia" y lo inicializamos en cero
    __motor = None # Creamos un atributo privado "__motor" y lo inicializamos en None
    
    # Creamos el constructor de la clase y le pasamos los parámetros de self, marca, color, potencia y motor
    def __init__(self, marca, color, potencia, motor):
        super().__init__(marca, color) # Herdamos los atributos de marca y color del constructor de la clase "Vehiculo()"
        self.__potencia = potencia # Al atributo "__potencia", le pasamos el valor del parámetro "potencia"
        self.__motor = motor # Al atributo "__motor", le pasamos el valor del parámetro "motor"
    
    # Creamos los métodos get para cada uno de los atributos de esta clase
    def getPotencia(self):
        return self.__potencia # Retornamos el valor de "__potencia"
    
    def getMotor(self):
        return self.__motor # Retornamos el valor de "__motor"
    
def main():
    # Pedimos que el usuario ingrese su nombre, la marca, el color, la potencia y motor del coche
    nombre = input("Bienvenido... Digita tu nombre: ")
    marca = input(f"{nombre} digita la marca del coche: ")
    color = input("Digita su color: ")
    potencia = eval(input("Ahora digita la potencia: "))
    motor = input("Digita el modelo del motor: ")
    
    # Instanciamos a la clase Coche dentro de una variable "coche" y enviamos los datos de marca, color, potencia y motor ingresados por el usuario
    coche = Coche(marca, color, potencia, motor)
    
    # Imprimimos todos los datos que ha ingresado el usuario
    print(f"{nombre} tu coche es de:\n"
          f"\nMarca: {coche.getMarca()}"
          f"\nColor: {coche.getColor()}"
          f"\nPotencia: {coche.getPotencia()}"
          f"\nModelo motor: {coche.getMotor()}")
    
if __name__ == "__main__":
    main()
