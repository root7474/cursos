// Principales operaciones aritméticas
let a = 3.5;
let b = 4.8;

// Suma
console.log(`${a} + ${b} = ${a + b}`);
// Resta
console.log(`${a} - ${b} = ${a - b}`);
// Multiplicación
console.log(`${a} x ${b} = ${a * b}`);
// División
console.log(`${a} / ${b} = ${a / b}`);
// Resto
console.log(`${a} % ${b} = ${a % b}`);

// Representación de números en cadenas de texto
let a_s = a.toString()

console.log(`Tipo de ${a}: ${typeof a}`);
console.log(a_s);
console.log(`Tipo de ${a_s}: ${typeof a_s}`);

// Redondeo de números decimales
let c = 3.3;
let d = c * 3;

console.log(`${c} * 3 = ${d}`);
console.log(`Tipo de ${d}: ${typeof d}`);

// toFixed(x) - Limitar el número de decimales al valor x
console.log(`${d} redondeado: ${d.toFixed(4)}`);
console.log(`Tipo de ${d} redondeado: ${typeof d.toFixed(4)}`);

let e = 1839.123456789;
let f = 2213556153215;

console.log(`${e} redondeado: ${e.toFixed(2)}`);
console.log(`${f} redondeado: ${f.toFixed(2)}`);

// toPrecision(x) - Limitar el número de cifras significativas
console.log(`Valor actual de ${e}: ${e.toPrecision(7)}`);
console.log(`Valor actual de ${f}: ${f.toPrecision(7)}`);
console.log(`Tipo de ${e.toPrecision(7)}: ${typeof e.toPrecision()}`);
console.log(`Tipo de ${f.toPrecision(7)}: ${typeof f.toPrecision()}`);
