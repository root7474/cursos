# Tarea: Clase alumno
# Autor: David Rodríguez

# Creamos una clase llamada "Alumno"
class Alumno():
    nombre = None # Creamos un atributo público llamado "nombre" y lo inicializamos en None
    __calificacion = 0 # Creamos un atributo privado llamado "__calificacion" y lo inicializamos en cero
    
    # Creamos el constructor de la clase con los prámetros de "nombre" y "calificacion"
    def __init__(self, nombre, calificacion):
        self.nombre = nombre # Le pasamos el valor del parámetro "nombre" al atributo "nombre" 
        self.__calificacion = calificacion # Le pasamos el valor del parámetro "calificacion" al atributo "__calificacion" 
    
    # Creamos un método get que devuelve el nombre del alumno
    def getNombre(self):
        return self.nombre
    
    # Creamos una función para evaluar si el alumno aprueba o no
    # Las calificaciones se evalúan de 0 a 10
    def __calificacionAlumno(self):
        if self.__calificacion >= 0 and self.__calificacion < 6:
            return f"{self.__calificacion}. No ha aprobado" # Si "__calificacion" es inferior que 6 hasta cero, entonces el alumno no aprueba
        elif self.__calificacion >= 6 and self.__calificacion <= 10:
            return f"{self.__calificacion}. Ha aprobado" # Si "__calificacion" es mayor o igual que 6 hasta 10, entonces el alumno aprueba
        else:
            return "Error!!!... La calificación ingresada es incorrecta" # Dado el caso de que ningúna condión sea correcta, generamos un error
    
    # Creamos un metodo get quedevuelve el valor de la función "__calificacionAlumno()"
    def getCalificacionAlumno(self):
        return self.__calificacionAlumno()
    
def main():
    # Pedimos al usuario que ingrese su nombre, el nombre del alumno y su calificación
    nombre = input("Bienvenido... Digita tu nombre: ")
    nombre_alumno = input(f"{nombre} digita el nombre de un alumno: ")
    calificacion = eval(input("Ahora digita su calificación: "))
    
    # Instanciamos dentro de una variable la clase "Alumno()" y le enviamos el nombre y la calificación del alumno
    alumno = Alumno(nombre_alumno, calificacion)
    print(f"{nombre} la calificación del alumno {alumno.getNombre()} es de: {alumno.getCalificacionAlumno()}") # Imprimimos por consola la calificación del alumno

if __name__ == "__main__":
    main()
