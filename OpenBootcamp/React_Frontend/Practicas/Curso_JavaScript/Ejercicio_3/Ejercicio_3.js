// Factorial de 10
// Autor: David Rodríguez

// Bucle For
let factorial = 1;

for (let i = 10; i > 0; i--) {
    factorial *= i;
}

console.log("Resultado con bucle For: " + factorial);

// Bucle While
let i = 10;
factorial = 1;

while (i > 0) {
    factorial *= i;
    i--;
}

console.log("Resultado con bucle While: " + factorial);

// Bucle Do...While y Break
i = 10;
factorial = 1;

do {
    factorial *= i;
    i--;

    if (i == 5) break;
} while (i > 0);

console.log(factorial);
