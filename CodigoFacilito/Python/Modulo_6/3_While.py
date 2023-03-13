def main():
    numero = 123456789
    contador_digitos = 0
    
    while numero >= 1:
        # contador_digitos = contador_digitos + 1
        contador_digitos += 1
        numero = numero / 10
    else:
        print("Fin del ciclo while")
        
    print(contador_digitos)
    
if __name__ == "__main__":
    main()
    