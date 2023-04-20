# Para la siguiente función, repetiremos los mismos pasos de la función "suma()" del módulo "Suma.py"
def division(cantidad):
    division = None
    print()
    
    try:
        for i in range(0, cantidad, 1):
            numero = eval(input(f"Digita el número {i + 1}: "))
            
            if division == None:
                division = numero
            else:
                division = division / numero
                
        return f"\nEl resultado de la división es: {round(division, 3)}"
    except(NameError):
        return "Error!!!... solo debes ingresar números"
    except(ZeroDivisionError):
        return "Error!!!... División por cero"
