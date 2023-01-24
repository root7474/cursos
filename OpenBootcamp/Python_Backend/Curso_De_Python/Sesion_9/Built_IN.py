# import _thread
# import time
# import logging
#from functools import reduce
from getpass import getpass

""" def horaActual(nombre_thread, tiempo_de_espera):
    count = 0
    
    while count < 5:
        time.sleep(tiempo_de_espera)
        count += 1
        print(f"Hilo: {nombre_thread} - {time.ctime(time.time())}") """

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def miFuncion(x):
    """ if x % 2 == 0:
        return True
    
    return False """
    
    """ if str(x).startswith("Pep"):
        return True
    
    return False """
    
    return x * x

def suma(a, b):
    print(f"a = {a}, b = {b}")
    return a + b
    
def main():
    """ _thread.start_new_thread(horaActual, ("Thread_uno", 1))
    _thread.start_new_thread(horaActual, ("Thread_dos", 2))
    
    print("He disparado ya los hilos")
    
    while True:
        pass """
        
    """ logging.basicConfig(level=logging.DEBUG)
    logging.debug("Prueba de debug")
    logging.info("Arrancando programa")
    logging.warning("Hace calor")
    logging.error("Test")
    logging.critical("Adios") """
    
    """ resultado = filter(miFuncion, ["Pepe", "Pepito", "Juan"])
    print(list(resultado)) """
    
    """ resultado_1 = map(miFuncion, numeros)
    print(list(resultado_1))
    
    resultado_2 = reduce(suma, numeros)
    print(resultado_2) """
    
    """ cursos = ["Python", "Java", "Git"]
    asistentes = [15, 20, 4]
    demo = zip(cursos, asistentes)
    print(list(demo)) """
    
    """ lista_A = [1 == 1, 2 == 2, 3 == 5]
    res = all(lista_A)
    print(res) """
    
    """ a = 5.5
    b = 5.4
    c = 5.6
    
    print(round(a))
    print(round(b))
    print(round(c)) """
    
    """ print(min(2, 3, 4, 5, 9, 3, 1))
    print(pow(2, 4)) """
    
    """ lista = ['z', 'c', 'd', 'a']
    ordenada = sorted(lista, reverse=True, key=lambda x: str(x).startswith('a'))
    print(ordenada) """
    
    user = input("Username: ")
    passwd = getpass("Password: ")
    print(user, passwd)
    
if __name__ == "__main__":
    main()
    

