// Ejercicio 4
// Autor David Rodríguez

// Cadenas para nombre, apellido y estudiante
let nombre = "David";
let apellido = "Rodríguez";
let estudiante = `${nombre} ${apellido}`;

// Imprimir cadena estudiante
console.log(estudiante);

// Cadena estudiante en mayúsculas
let estudianteMayus = estudiante.toUpperCase();
console.log(estudianteMayus);

// Cadena estudiante en minúsculas
let estudianteMinus = estudiante.toLowerCase();
console.log(estudianteMinus);

// Imprimir el número de letras de la cadena estudiante
let numLetrasEstudiante = estudiante.length;
console.log(numLetrasEstudiante)

// Imprimir la primera letra del nombre
let primeraLetra = nombre[0];
console.log(primeraLetra);

// Imprimir la última letra del apellido
let ultimaLetra = apellido[apellido.length - 1];
console.log(ultimaLetra);

// Variable para saber si el nombre está contenido dentro de la variable estudiante
// let confirmaNombre = Boolean(nombre, estudiante));

let confirmaNombre = estudiante.includes(nombre);
console.log(confirmaNombre);
