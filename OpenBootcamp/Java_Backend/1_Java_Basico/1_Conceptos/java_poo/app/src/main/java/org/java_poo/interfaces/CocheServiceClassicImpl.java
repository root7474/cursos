package org.java_poo.interfaces;

import org.java_poo.Coche;
import org.java_poo.CocheElectrico;

public class CocheServiceClassicImpl implements CocheService {
    @Override
    public Coche crearCocheDemo() {
        // TODO Auto-generated method stub
        System.out.println("Creando coche clásico");
        return new CocheElectrico();
    }

    @Override
    public void destruirCoche(Coche coche) {
        // TODO Auto-generated method stub
        System.out.println("Destruyendo coche");
    }
}
