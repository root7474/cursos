// Métodos más utilizados con cadena de caracteres (parte 2)
let input = "eScorPio";
let db = "escorpio";

// toLowerCase() - toUpperCase()
console.log(`Minúsculas: ${input.toLowerCase()}`);
console.log(`Mayúsculas: ${input.toUpperCase()}`);
console.log(`${input.toLowerCase()} = ${input.toUpperCase()}: ${input.toLowerCase() === input.toUpperCase()}`);
console.log(`${input.toUpperCase()} = ${input.toUpperCase()}: ${input.toUpperCase() === input.toUpperCase()}`);

// Formas de concatenar cadenas
let str_1 = "Hola soy la primera cadena.";
let str_2 = "Y yo soy la segunda cadena";

console.log(str_1.concat(" ", str_2));
console.log(str_1 + " " + str_2);
console.log(`${str_1} ${str_2}`);

// Eliminar espacios al inicio y al final
let str_3 = "   Hola soy un string con espacios al final.   ";
console.log(str_3.length);

// trim()
console.log(str_3.trim().length);
console.log(str_3.trimStart().length);
console.log(str_3.trimEnd().length);

// charAt(x)
let str_4 = "Hola soy el string número 4"; // ["H", "o", "l", "a", " ", "s"...]
console.log(str_4.charAt(5));
console.log(str_4[5]);

// Obtener la posición de una palabra dentro de una cadena de caracteres
let str_5 = "Hola soy David y me gusta el fútbol. Mi nombre es David y mi apellido es Rodríguez";
console.log(`Posición: ${str_5.indexOf("soy David")}`);
console.log(str_5.charAt(5));
console.log(`Posición: ${str_5.lastIndexOf("David")}`);
console.log(str_5.charAt(50));
