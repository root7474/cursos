package org.arrays;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // int[] notas = new int[10];
        int[] notas2 = {8, 10, 5, 9, 8, 7, 5, 6};
        int[] notas3 = {8, 10, 5, 9, 8, 7, 5, 6};
        
        // notas[0] = 8;
        // notas[1] = 9;

        // System.out.println(notas[0]);
        
        // for()
        /* for(int i = 0; 1 < notas2.length; i++) {
            System.out.println(notas2[i]);
        }

        // foreach()
        for(int item : notas2) {
            System.out.println(item);
        } */

        Arrays.binarySearch(notas2, 9);
        Arrays.sort(notas2);
        Arrays.equals(notas2, notas3);
    }
}
