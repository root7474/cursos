// Formas de importar y exportar módulos
// 1. CommonJS - require
// 2. Import ES6 - import
// const moduloMatematicas = require("./modulos/matematicas");
// console.log(moduloMatematicas.eleva);

const {factorial, suma} = require("./modulos/matematicas")

const fact = factorial(5);
console.log(fact);

const sum = suma(12, 90);
console.log(sum);

/* const fact = factorial(5);
console.log(fact);

const sum = suma(12, 90);
console.log(sum); */
