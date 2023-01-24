import pickle

class Juguete:
    nombre = ""
    precio = 0.0
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def getNombre(self):
        return self.nombre
    
""" j1 = Juguete("Potato", 10.5)
f = open ("/home/root7474/Documents/Cursos/OpenBootcamp/Python_Backend/Curso_De_Python/Sesion_8/datos.bin", "wb")
pickle.dump(j1, f)
f.close() """

f = open("/home/root7474/Documents/Cursos/OpenBootcamp/Python_Backend/Curso_De_Python/Sesion_8/datos.bin", "rb")
potato = pickle.load(f)
f.close()

print(type(potato))
print(f"{potato.getNombre()} precio: {potato.precio}")
