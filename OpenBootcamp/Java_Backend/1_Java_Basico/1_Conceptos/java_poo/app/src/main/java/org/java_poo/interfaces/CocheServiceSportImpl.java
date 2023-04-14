package org.java_poo.interfaces;

import org.java_poo.Coche;

public class CocheServiceSportImpl implements CocheService {

    @Override
    public Coche crearCocheDemo() {
        // TODO Auto-generated method stub
        System.out.println("Creando coche de carreras");
        return null;
    }

    @Override
    public void destruirCoche(Coche coche) {
        // TODO Auto-generated method stub
        System.out.println("Destruyendo coche");
    }
    
}
