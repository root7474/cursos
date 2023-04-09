// Operador valueOf() - Obtener valores numéricos a partir de literales
let a = 2;
let b = new Number(3);

console.log(`Número: ${a}`);
console.log(`Número: ${b}`);
console.log(`${a} + ${b} = ${a + b}`);
console.log(`${a} + ${b} = ${a.valueOf() + b.valueOf()}`);
console.log(`Número: ${b.valueOf()}`);

// NaN (Not a Number) - Infinity
let c = Number("Adiós");
console.log(`Número: ${c}`);
console.log(`C no es un número?: ${isNaN(c)}`);

let numerador = 19;
let divisor_1 = 0;
let divisor_2 = null;

console.log(`${numerador} / ${divisor_1} = ${numerador / divisor_1}`);
console.log(`${numerador} / ${divisor_2} = ${numerador / divisor_2}`);

// Cómo convertir los strings a valores numéricos con Number, parseInt y parseFloat
let numero_1 = "5.89";
let numero_2 = 17.2;

console.log(`Tipo actual de ${numero_1}: ${typeof numero_1}`);
console.log(numero_1 + numero_2); // Error de concepto
console.log(`${numero_1} + ${numero_2} = ${Number(numero_1) + numero_2}`);

// parseInt()
console.log(`Número entero: ${parseInt(numero_1)}`);
// parseFolat()
console.log(`Número decimal: ${parseFloat(numero_1)}`);

let numero_3 = 4;
console.log(`Número entero: ${parseInt(numero_3)}`);
console.log(`Número decimal: ${parseFloat(numero_3)}`);

// Números hexadecimales (base 16)
let numHex = "0x3a5b7";
console.log(parseInt(numHex, 16));

// Obtener los valores máximos y minimos de JavaScript
let min_precision = Number.EPSILON;
let min_valor_JS = Number.MIN_VALUE;
let max_valor_JS = Number.MAX_VALUE;

console.log(`Precisión mínima de JavaScript: ${min_precision}`);
console.log(`Valor mínimo de JavaScript: ${min_valor_JS}`);
console.log(`Valor máximo de JavaScript: ${max_valor_JS}`);
console.log(`2 ^ 1023 = ${2 ** 1023}`);
