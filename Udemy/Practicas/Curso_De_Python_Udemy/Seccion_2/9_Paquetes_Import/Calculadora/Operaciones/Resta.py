# Para la siguiente función, repetiremos los mismos pasos de la función "suma()" del módulo "Suma.py"
def resta(cantidad):
    resta = None
    print()
    
    try:
        for i in range(0, cantidad, 1):
            numero = eval(input(f"Digita el número {i + 1}: "))
            
            if resta == None:
                resta = numero
            else:
                resta = resta - numero
                
        return f"\nEl resultado de la resta es: {resta}"
    except(NameError):
        return "Error!!!... solo debes ingresar números"