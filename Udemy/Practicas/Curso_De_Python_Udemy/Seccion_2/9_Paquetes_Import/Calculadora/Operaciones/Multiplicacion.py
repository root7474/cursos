# Para la siguiente función, repetiremos los mismos pasos de la función "suma()" del módulo "Suma.py"
def multiplicacion(cantidad):
    multiplicacion = None
    print()
    
    try:
        for i in range(0, cantidad, 1):
            numero = eval(input(f"Digita el número {i + 1}: "))
            
            if multiplicacion == None:
                multiplicacion = numero
            else:
                multiplicacion = multiplicacion * numero
                
        return f"\nEl resultado de la multiplicación es: {multiplicacion}"
    except(NameError):
        return "Error!!!... solo debes ingresar números"