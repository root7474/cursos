# Creamos una fución "porcentaje()" que tendrá como parámetro una constante que recibe como valor el número 100
def porcentaje(NUMERO_PORCENTAJE):
    try:
        numero = eval(input("Digita un número para clacular su porcentaje: ")) # Pedimos al usuario que ingrese un número
        resultado = numero / NUMERO_PORCENTAJE # Caculamos el porcentaje del número ingresado haciendo una división entre 100
        
        return f"El prcentaje de {numero} es: {resultado}" # Retornamos el resultado de dicho porcentaje
    except(NameError):
        return "Error!!!... solo debes ingresar números" # Esto se ejecutará si se han ingresado letras o caracteres especiales
