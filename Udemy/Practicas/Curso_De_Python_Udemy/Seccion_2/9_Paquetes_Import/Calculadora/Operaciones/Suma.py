# Creamos un función "suma" con el parámetro "cantidad" que recibe la cantidad entera que ingrese el usuario
def suma (cantidad):
    suma = None # Declaramos una variables "suma" que recibe un valor nulo por defecto
    print() # Ponemos un salto de línea
    
    # Se ejecutará lo siguiente si no se han ingresado letras o caracteres especiales
    try:
        for i in range(0, cantidad, 1): # Recorremos la cantidad ingresada por el usuario
            numero = eval(input(f"Digita el número {i + 1}: ")) # En cada iteración pedimos que se ingrese un valor numérico sea decimal o entero
            
            if suma == None:
                suma = numero # Si la variable "suma" es nula, recibirá el valor de la variable "numero"
            else:
                suma = suma + numero # Si la variable "suma" no es nula, haremos una suma del valor de "suma" + el valor de "numero" en cada iteración
                
        return f"\nEl resultado de la suma es: {suma}" # Retornamos el resultado de la operación de suma
    except(NameError):
        # Saltaremos al error si se han ingresado letras o caracteres especiales
        return "Error!!!... solo debes ingresar números"
