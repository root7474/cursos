// Exercise of primitive types in Java
// Author: David Rodríguez
package org.example;

public class Main {
    public static void main(String[] args) {
        // Numerics
        byte myNum1 = 127;
        short myNum2 = 32767;
        int myNum3 = 2147483647;
        long myNum4 = 9223372036854775807L;

        // Float point
        float myNum5 = 27.1234567F;
        double myNum6 = 27.1234567891012131;

        // Booleans
        boolean myBoolean = true;

        // Characters
        String myString = "Hello! My name is David and I am from Colombia"; // Strings
        char myChar = 'a'; // Chars

        System.out.println("Number 1: " + myNum1);
        System.out.println("Number 2: " + myNum2);
        System.out.println("Number 3: " + myNum3);
        System.out.println("Number 4: " + myNum4);
        System.out.println("Number 5: " + myNum5);
        System.out.println("Number 6: " + myNum6);
        System.out.println("True or false: " + myBoolean);
        System.out.println("Message: " + myString);
        System.out.println("Character: " + myChar);
    }
}