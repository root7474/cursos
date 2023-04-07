from random import randint as azar
# from random import *

def main():
    continuar = 's'
    
    while(continuar == 's' or continuar == 'S'):
        lanza_dado = azar(1, 6)
        print(f"Haz sacado un: {lanza_dado}")
        
        continuar = input("Continuamos (s/S/n): ")
    print("Ya no tiro más dados, hasta luego")
    
if __name__ == "__main__":
    main()
    