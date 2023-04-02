// Segundo programa que calcula el factorial de 10 con ciclo while
// Autor: David Rodríguez
// Declaramos una variable inicial con valor de 10 y una variable contador con valor de 10 - 1
let numero = 10;
let contador = numero - 1;

// Si número es igual a 0 o si número es igual a 1, entonces el factorial de numero es 1
if (numero === 0) numero = 1;

// Hacemos el cálculo multiplicando el valor de numero por el valor de i
// Y guardaremos su resultado dentro de numero en cada iteración
while (contador >= 1) {
    if (numero === 1) {
        numero = 1;
        break;
    }

    numero = numero * contador;
    contador--;
}

console.log(numero);
