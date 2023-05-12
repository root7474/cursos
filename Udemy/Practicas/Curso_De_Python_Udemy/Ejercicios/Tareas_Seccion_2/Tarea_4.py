# Tarea 4: Modifica variables
# Autor: David Rodríguez

""" En el anterior ejercicio usamos la función "eval()"
para convertir un tipo de dato string a un tipo numérico
como en el caso de la variable "edad" que ecuando imprimimos 
su tipo por pantalla, nos daba que la variable era de tipo entero.
En este caso usamos la función "int()" para convertir un string a un entero
que hace lo mismo que la función "eval()". La diferencia es que en "eval()",
el interprete se encarga de transformar el tipo del valor de la variable 
al tipo que mejor represente a ese valor, mientras que la función "int()",
solo convierte el tipo de dato de la variable a enteros """

def main():
    # Pedimos datos de usurio como el nombre y la edad
    nombre = input("Digita tu nombre: ")
    edad = int(input("Digita tu edad: ")) # Convertimos la edad que ingrese el usuario a un tipo de dato entero
    
    # Imprimimos los datos que ha ingresado el usuario y sus tipos por consola
    print(f"Nombre: {nombre}"
          f"\nEdad: {edad}"
          f"\n\nTipo de dato de nombre: {type(nombre)}"
          f"\nTipo de dato de edad: {type(edad)}")

if __name__ == "__main__":
    main()
