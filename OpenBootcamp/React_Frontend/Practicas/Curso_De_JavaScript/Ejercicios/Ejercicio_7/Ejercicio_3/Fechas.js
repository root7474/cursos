// Ejercicio 3: Fechas
// Autor: David Rodríguez
// Creamos una variable "fechaHoy" que contendrá la fecha actual
let fechaHoy = new Date();
console.log(`Fecha de hoy: ${fechaHoy.toLocaleDateString("en-GB")}`);

// Creamos otra variable "fechaNacimiento" que contendrá la fecha de nacimiento
let fechaNacimiento = new Date("February 5, 1996");
console.log(`Fecha de nacimiento: ${fechaNacimiento.toLocaleDateString("en-GB")}`);

// Verificamos si hoy es más tarde que nuestra fecha de nacimiento
//  y guardamos su resultado dentro de la variable "compararFechas"
let compararFechas = fechaHoy > fechaNacimiento;
console.log(`"${fechaHoy.toLocaleDateString("en-GB")}" es más tarde que "${fechaNacimiento.toLocaleDateString("en-GB")}"?: ${compararFechas}`);

// Creamos una variable "diaNacimiento" que recibirá el día de nuestra fecha de nacimiento
let diaNacimiento = fechaNacimiento.getDate()
console.log(`Día de nacimiento: ${diaNacimiento}`);

// Creamos una variable "mesNacimiento" que recibirá el mes de nuestra fecha de nacimiento
let mesNacimiento = fechaNacimiento.getMonth() + 1;
console.log(`Mes de nacimiento: {mesNacimiento}`);

// Creamos una variable "añoNacimiento" que recibirá el año de nuestra fecha de nacimiento
let añoNacimiento = fechaNacimiento.getFullYear();
console.log(`Año de nacimiento: ${añoNacimiento}`);
