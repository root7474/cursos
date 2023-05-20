// Trabajando con fechas
const fecha = new Date();
console.log(fecha);

// Atención los meses se incializan en 0 (0 Enero - 11 Diciembre)
const fecha2 = new Date(1987, 10, 20, 1, 23, 52, 192);
console.log(fecha2);

const fecha3 = new Date(-1000000000000);
console.log(fecha3);

const fecha4 = new Date("February 5, 1996 12:0:0");
console.log(fecha4);
console.log(fecha > fecha4);

const fecha5 = new Date(1987, 10, 20, 1, 23, 52, 192);
console.log(fecha5);
console.log(fecha2 === fecha3); // Error no se pueden comparar fechas de esta manera
console.log(fecha2.getTime() == fecha5.getTime()); // Ok - ESta es la forma de comparar la igualdad entre fechas

// Obtener el día, el mes y el año de una fecha
// Obtner el día - getDate()
console.log(fecha2.getDate());

// Obtner el mes - getMonth()
console.log(fecha2.getMonth());

// Obtner el año - getYear()
console.log(fecha2.getFullYear());
console.log(fecha2);

// toLocaleDateString()
// https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleDateString
console.log(fecha2.toLocaleDateString("en-GB"));
