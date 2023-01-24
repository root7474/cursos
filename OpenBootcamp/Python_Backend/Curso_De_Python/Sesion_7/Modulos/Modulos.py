# import Operaciones
""" import sys
sys.path.append("/home/root7474/Documents/Cursos/OpenBootcamp/Python_Backend/Curso_De_Python/Sesion_7/Demo_Saluda")

import Saluda
import pprint """

# import Operaciones.Suma
""" import Operaciones.Sumador.Suma as s
import Operaciones.Restador.Resta as r """

# from Operaciones import *
import Operaciones.Sumador.Suma as s
import pprint

def main():
    """ res_suma = Operaciones.suma(2,2)
    res_resta = Operaciones.resta(5, 3)
    op = Operaciones.Operador()
    
    print("Hola en main()", res_suma, res_resta)
    print(Operaciones.como_me_llamo())
    print(op.multiplicccion(4, 2))
    print(Operaciones.PI) """
    
    # pprint.pprint(sys.path)
    # Saluda.saluda("David")
    """ mp = Operaciones.Suma.Multiplicador()
    print(mp.multiplica(5, 5)) """
    
    """ Restador.resta(5, 3)
    Sumador.suma(4, 3) """
    
    obj = s.Sumatorio()
    obj.suma(2, 2)
    
    help(obj.suma)
    
    """ tupla = ()
    pprint.pprint(dir(tupla)) """
    
if __name__ == '__main__':
    main()
