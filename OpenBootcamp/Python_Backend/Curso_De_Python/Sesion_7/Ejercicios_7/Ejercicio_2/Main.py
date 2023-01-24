# Ejercicio 2, sesión 7
# Autor: David Rodríguez

# Importamos el módulo time
import time

def main():
    # Invocamos a las funciones time() y localtime() para saber nuestra hora local
    tiempo_segundos = time.time()
    tiempo_local = time.localtime(tiempo_segundos)

    # Hora para despertarse e ir al trabajo
    if tiempo_local.tm_hour == 7:
        print(f"Despierta son las {tiempo_local.tm_hour}. Es hora de ir al trabajo :'(")
    
    # Tiempo de permanencia en el trabajo
    if (tiempo_local.tm_hour >= 9 and tiempo_local.tm_min >= 0) and tiempo_local.tm_hour < 12:
        print(f"Son las {tiempo_local.tm_hour} y {tiempo_local.tm_min}. Aún debes trabajar :'(")
    
    # Tiempo para el almuerzo
    if (tiempo_local.tm_hour >= 12 and tiempo_local.tm_min >= 0) and tiempo_local.tm_hour < 14:
        print(f"Son las {tiempo_local.tm_hour}. Es la hora de almorzar :D")
    
    # Tiempo para volver al trabajo
    if (tiempo_local.tm_hour >= 14 and tiempo_local.tm_min >= 0) and tiempo_local.tm_hour < 19:
        print(f"Son las {tiempo_local.tm_hour} y {tiempo_local.tm_min}. Es hora de trabajar :'(")
    
    # Hora para volver a casa
    if tiempo_local.tm_hour == 19:
        print(f"Son las {tiempo_local.tm_hour}. Es hora de ir a casa :D")
        
if __name__ == "__main__":
    main()
