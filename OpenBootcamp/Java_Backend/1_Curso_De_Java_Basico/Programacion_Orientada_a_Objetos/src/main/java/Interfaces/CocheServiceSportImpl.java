package Interfaces;

import org.company.Coche;
import org.company.CocheElectrico;

public class CocheServiceSportImpl implements CocheService {

    @Override
    public Coche crearCocheDemo() {
        // TODO Auto-generated method stub
        System.out.println("Creando un coche deportivo");
        return new CocheElectrico();
    }

    @Override
    public void destruirCoche(Coche coche) {
        // TODO Auto-generated method stub
        System.out.println("Destruyendo coche");
    }
    
}
