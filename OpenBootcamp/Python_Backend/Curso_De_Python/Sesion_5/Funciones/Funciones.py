def operaciones(a, b):
    return a + b, a - b, a * b, a / b

def sumador(**kwargs):
    inicial = kwargs["inicial"] if "inicial" in kwargs else 0
    final = kwargs["final"] if "final" in kwargs else inicial
    
    resultado = 0
    
    for i in range(inicial, final + 1):
        resultado += i
        
    return resultado

print(sumador(final = 5))

# Funciones anónimas o lambdas
anonima = lambda nombre, nombre2: print(f"Hola {nombre} adios {nombre2}")
anonima("David", "Andrés")

resultado = lambda x: x * x
print(resultado(2))
