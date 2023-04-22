package org.arrays_practica;

import java.util.Arrays;

public class ArraysMain {
    public static void main(String[] args) {
        /* int[] notas1 = new int[10];

        notas1[0] = 8;
        notas1[1] = 9;
        System.out.println(notas1[0]); */

        int[] notas2 = {8, 10, 5, 9, 8, 7, 5, 6};
        int[] notas3 = {8, 10, 5, 9, 8, 7, 5, 6};

        // for()
        /* for (int i = 0; i < notas2.length; i++) {
            System.out.println("Número " + (i + 1) + ": " + notas2[i]);
        } */

        // foreach()
        /* for (int item : notas2) {
            System.out.println(item);
        } */

        System.out.println(Arrays.binarySearch(notas2, 9));
        Arrays.sort(notas2);
        System.out.println(Arrays.equals(notas2, notas3));
    }
}
