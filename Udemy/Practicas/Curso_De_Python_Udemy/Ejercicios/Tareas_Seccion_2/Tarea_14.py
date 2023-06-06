# Tarea: Modulo DateTime
# Autor: David Rodríguez
# Importamos el módulo "datetime" y le asignamos un alias
from datetime import datetime as dt

# Creamos una función que4 se encargará de generar una alarma
# Que nos notifique sobre el fin de la jornada laboral 
# Le pasamos como parámetros la hora y los minutos
def fin_jornada_laboral(hora, minutos):
    condicion_while = False # Declaramos un variable condicional para esta función y la inicializamos en False
    
    # Haremos lo siguiente mientras la condición declarada sea igual a False
    while condicion_while == False:
        hora_actual = dt.now() # Instanciamos dentro de una variable a la función "now()" del módulo "datetime"
        print(f"Son las {hora_actual.hour}:{hora_actual.minute}") # En cada iteración imprimimos la hora actual en horas y minutos
        
        # Si la hora y los minutos son menores a los datos ingresados por el usuario
        if hora_actual.hour >= hora and hora_actual.minute >= minutos:
            condicion_while = True # El valor de la variable condicional será True
            return True # retornamos un valor de True si la condición se cumple
    
    return False # Si la condición no se cumple, retornamos un valor de False

# A continuaciòn, creamos las validaciones correspondientes a la hora y a los minùtos ingresados
# Creamos una función para validar la hora y le pasamos como parámetro una cadena de caracteres
def validar_hora(mensaje):
    data = 0 # Declaramos una variable "data" para guardar los datos ingresados por el usuario
    condicion_while = False # Declaramos un variable condicional para esta función y la inicializamos en False
    
    # Haremos lo siguiente mientras la condición declarada sea igual a False
    while condicion_while == False:
        try:
            # Generamos un bloque try para validar los datos que se ingresen por consola
            data = int(input(mensaje)) # Recibimos los datos que ingrese el usuario y lo convertimos a enteros
            
            if data < 0 and data > 23:
                print("Error!!!... Debes digitar una hora no menor a cero y no mayor a 23") # Si la hora ingresada es menor a cero y mayor a 23, imprimimos este error
            else:
                condicion_while = True # Si todo está correcto, el valor de la condición será igual a True y se romperá el ciclo
        except ValueError:
            print("Error!!!... Debes ingresar una cantidad de horas correcta") # Si lo que se ha ingresado no es un número entero, imprimimos este error
    
    return data # Retornamos el valor de "data"

# Creamos una función para validar los minutos y le pasamos como parámetro una cadena de caracteres
# Para esta función seguiremos los pasos de la anterior función
def validar_minutos(mensaje):
    data = 0
    condicion_while = False
    
    while condicion_while == False:
        try:
            data = int(input(mensaje))
            
            if data < 0 and data > 59: 
                print("Error!!!... Debes digitar una cantidad de minutos no menor a cero y no mayor a 59") # Si los minutos ingresados son menores a cero y mayores a 59, imprimimos este error
            else:
                condicion_while = True
        except ValueError:
            print("Error!!!... Debes ingresar una cantidad de minutos correcta")
    
    return data

# Creamos una función para recibir los datos que ingrese el usuario por consola y le pasamos como parámetro el nombre del usuario
def datos_usuario(nombre):
    hora = validar_hora(f"{nombre} Digita una hora: ") # Llamamos a la función "validar_hora()" y le enviamos un string con el nombre del usuario
    minutos = validar_minutos("Digita los minutos: ") # Llamamos a la función "validar_minutos()" y le enviamos una cadena de caracteres
    
    fin_jornada = fin_jornada_laboral(hora, minutos) # Llamamos a la función "fin_jornada_laboral()" y le enviamos la hora y los minutos ingresados
    if fin_jornada == True: print(f"{nombre} tu jornada laboral ha terminado") # Si el valor de la función "fin_jornada_laboral()" retorna True, imprimimos este mensaje

def main():
    nombre = input("Bienvenido... \nDigita tu nombre: ") # Pedimos al usuario que ingrese su nombre
    datos_usuario(nombre) # Enviamos el nombre del usuario a la función "datos_usuario()"

if __name__ == "__main__":
    main()
