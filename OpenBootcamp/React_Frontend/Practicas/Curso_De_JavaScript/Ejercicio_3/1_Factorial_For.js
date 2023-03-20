// Programa que calcula el factorial de 10 con ciclo for
// Autor: David Rodríguez
let numero = 10;

// Si número es igual a 0 o si número es igual a 1, entonces el factorial de numero es 1
if (numero === 0) numero = 1;
if (numero === 1) numero = 1;

// Hacemos el cálculo multiplicando el valor de numero por el valor de i
// Y guardaremos su resultado dentro de numero en cada iteración
for (let i = numero - 1; i >= 1; i--) {
    numero = numero * i;
}

console.log(numero); // Imprimimos el valor actual de la variable numero
