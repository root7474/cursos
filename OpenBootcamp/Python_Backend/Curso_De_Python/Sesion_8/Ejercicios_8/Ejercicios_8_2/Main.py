from Modules.Vehiculo import Vehiculo
import pickle

def cargarArchivo():
    f = open("Salida.bin", "rb")
    salida_binarios = pickle.load(f)
    
    f.close()
    
    print(f"\nTipo: {salida_binarios.getTipo()}" 
          f"\nMarca: {salida_binarios.getMarca()}"
          f"\nModelo motor: {salida_binarios.getMotor()}"
          f"\nNúmero de ventanas: {salida_binarios.getVentanas()}"
          f"\nNúmero de puertas: {salida_binarios.getPuertas()}\n")

def main():
    vehiculo = Vehiculo()
    f = open("Salida.bin", "wb")
    
    tipo = input("\nDigita el tipo de vehículo (E.j.: Moto, Coche, etc): ")
    marca = input("Digita la marca del vehículo: ")
    color = input("Digita su color: ")
    motor = input("Digita el modelo de su motor: ")
    
    condicion_1 = input("Tu vehículo tiene ventanas? (Si, No): ")
    
    if condicion_1 == "Si":
        ventanas = eval(input("Cuantas ventanas tiene tu vehículo?: "))        
        vehiculo.setVentanas(ventanas)
    if condicion_1 == "No":
        ventanas = 0
        vehiculo.setVentanas(ventanas)
    
    condicion_2 = input("Tu vehículo tiene puertas? (Si, No): ")
    
    if condicion_2 == "Si":
        puertas = eval(input("Cuantas puertas tiene tu vehículo?: "))
        vehiculo.setPuertas(puertas)
    if condicion_2 == "No":
        puertas = 0
        vehiculo.setPuertas(puertas)
    
    vehiculo.setTipo(tipo)
    vehiculo.setMarca(marca)
    vehiculo.setColor(color)
    vehiculo.setMotor(motor)
    
    pickle.dump(vehiculo, f)
    f.close()
    
    cargarArchivo()
    
if __name__ == "__main__":
    main()
