def funcion1(n):
    if (n >= 0 ):
        print(n, end=' -> ')
        funcion1(n - 1)
    else:
        print("Limite 1")
        
def funcion2(n):
    if (n >= 0):
        funcion2(n - 1)
        print(n, end=' -> ')
    else:
        print("Limite 2")

print("Usando función 1: ")
funcion1(10)
print("\nUsando función 2: ")
funcion2(10)
