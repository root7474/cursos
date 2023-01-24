from OpenBootcamp.Python_Backend.Curso_De_Python.Sesion_6.Programacion_Orientada_A_Objetos.Clases_Y_Objetos.Composiciones import Carroceria


class Categorias:
    idcategoria = 0
    nombre = ""
        
class Proveedores:
    idcategoria = 0
    nombre = ""
    
class Productos:
    idproducto = 0
    CategoriaProducto = Categorias()
    Precio = 0
    Tamaño = 0
    TipoDeProducto = 0
    CIFProveedor = Proveedores()

def main():
    p = Productos()
    p.CIFProveedor.nombre
    p.CategoriaProducto.idcategoria
