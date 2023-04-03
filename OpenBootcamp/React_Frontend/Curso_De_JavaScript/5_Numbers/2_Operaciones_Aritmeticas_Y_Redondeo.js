// Principales operaciones aritméticas
let a = 3.5;
let b = 4.8;

// Suma
console.log(`${a} + ${b} = ${a + b}`);
// Resta
console.log(`${a} - ${b} = ${a - b}`);
// Multiplicación
console.log(`${a} * ${b} = ${a * b}`);
// División
console.log(`${a} / ${b} = ${a / b}`);

// Representación de números en cadenas de texto
console.log(`Tipo de ${a}: ${typeof a}`);

let a_s = a.toString();
console.log(a_s);

// Redondeo de números decimales
let c = 3.3;
let d = c * 3;

console.log(d);
console.log(typeof d);

// toFixed(x) - Limitar el número de decimales al valor x
console.log(d.toFixed(4));
console.log(typeof d.toFixed(4));

let e = 1839.123456789;
let f = 2213556153215;

console.log(e.toFixed(2));
console.log(f.toFixed(2));

// toPrecision(x) - Limitar el número de cifras significativas
console.log(e.toPrecision(7));
console.log(f.toPrecision(7));

console.log(typeof e.toPrecision(7));
console.log(typeof f.toPrecision(7));
