package com.ejercicio_modulo_3;

 /**
  * Programa para calcular el precio total de un producto
  * Autor: David Rodríguez
  */

public class Main {
    /**
     * Creamos una función Main() para ejecutar nuestro programa
     * @param args
     */

    public static void main(String[] args) {
        /* 
         * Creamos una variable precioProducto
         * Llamamos a la función precioTotal() y le pasamos como parámetro
         * A la variable precioProducto
         * Guardamos el resultado dentro de la variable llama precioTotalProducto
         * Imprimimos el resultado por consola
         */

        double precioProducto = 4.55;
        double precioTotalProducto = precioTotal(precioProducto);
        System.out.println("Precio más IVA incluido: " + precioTotalProducto);
    }

    /**
     * Creamos una función precioTotal() que retorna el precio de un producto incluído su IVA
     * @param precioProducto
     * @return
     */

    private static double precioTotal(double precioProducto) {
        return precioProducto + 5.55;
    }
}
