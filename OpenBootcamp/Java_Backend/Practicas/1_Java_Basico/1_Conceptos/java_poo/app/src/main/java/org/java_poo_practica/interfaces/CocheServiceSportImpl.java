package org.java_poo_practica.interfaces;

import org.java_poo_practica.Coche;
import org.java_poo_practica.CocheElectrico;

public class CocheServiceSportImpl implements CocheService {
    public Coche crearCocheDemo(){
        System.out.println("Creando coche deportivo");
        return new CocheElectrico();
    }

    public void destruirCoche(Coche coche) {
        System.out.println("Destruyendo coche");
    }
}
