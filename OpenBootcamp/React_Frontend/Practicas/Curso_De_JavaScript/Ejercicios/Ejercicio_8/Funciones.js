// Ejercicio #8: Funciones
// Autor: David Rodríguez

// 1.) Creamos una función sin parámetros llamada "verdadero"
function verdadero() {
    return true; // Esta función siempre nos va a devolver true
}

console.log(verdadero()); // Imprimimos por consola el valor de la función

// 2.) Creamos una función asíncrona llamada "promesa()"
// Esta función tiene como parámetro un contador para agregarle recursividad a la función
async function promesa(contador) {
    if (contador === 5) return; // Si contador es igual a 5, la función ya no retornará nada
    promesa(contador + 1); // Llamamos a la función y le pasamos como parámetro a contador + 1
    return setTimeout(() => console.log(`${contador + 1}.) Hola soy una promesa`), 5000); // Retornamos el mensaje "Hola soy una promesa" después de 5 segundos
}

console.log(promesa(0)); // IMprimimos por consola el valor de la función pasándole como parámetro el cero

// 3.) Creamos una función generadora llamada "generarPares()" y le pasamos como parámetro un contador
function* generarPares(contador) {
    while (true) {
        if (contador % 2 === 0) yield contador; // Si el residuo de la división entre contador y 2 es cero, retornaremos un número par
        contador++; // Incrementamos a contador en 1
    }
}

// Guaradamos a la función "generarPares()" dentro de la variable "id" y le pasamos como prámetro el número cero
let id = generarPares(0);
let cantidad = 5; // Creamos una variable cantidad y le asignamos el valor de 5

// Recorremos dicha cantidad y en cada iteración, mostramos el valor de id
for (let i = 0; i < cantidad; i++) console.log(`id ${i + 1}: ${id.next().value}`);
