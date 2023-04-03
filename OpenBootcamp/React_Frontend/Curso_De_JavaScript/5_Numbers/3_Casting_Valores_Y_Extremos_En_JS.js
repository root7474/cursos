// Operador valueOf() - Obtener valores numéricos a partir de literales
let a = 2;
let b = new Number(3);

console.log(a);
console.log(b);
console.log(a + b);
console.log(a.valueOf() + b.valueOf());
console.log(b.valueOf());

let str = new String("Hola soy un string");
console.log(str);
console.log(str.valueOf());

// NaN (Not a Number) - Infinity
let n = Number("Adiós")
console.log(n);
console.log(isNaN(n));

let numerador = 19;
let divisor = 0;
let divisor_2 = null;

console.log(numerador / divisor);
console.log(numerador / divisor_2);

// Cómo convertir los strings a valores numéricos con Number, parseInt y parseFloat
let numero = "5.89";
let numero_2 = 17.2;

console.log(typeof numero);
console.log(numero + numero_2); // Error de concepto
console.log(Number(numero) + numero_2);

// parseInt()
console.log(parseInt(numero));

// parseFloat()
console.log(parseFloat(numero));

let numero_3 = 4;
console.log(parseInt(numero_3));
console.log(parseFloat(numero_3));

// Números hexadecimales (base 16)
let numHex = "0x3a5b7";
console.log(parseInt(numHex, 16));

// Obtener los valores máximos y minimos en JavaScript
let min_precision = Number.EPSILON;
let min_valor_JS = Number.MIN_VALUE;
let max_valor_js = Number.MAX_VALUE;

console.log(min_precision);
console.log(min_valor_JS);
console.log(max_valor_js);
console.log(2 ** 1023);
