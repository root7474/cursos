// Ejercicio - 5
// Autor: David Rodríguez

// Creamos las variables "alturaCentimetros", "alturaMetros" y "pesoKilogramos"
let alturaCentimetros = 166;
let alturaMetros = 1.66;
let pesoKilogramos = 55.5;

// Creamos una variable que contendrá la altura redondeada hacia arriba
let alturaMetrosUp = Math.ceil(alturaMetros);
console.log(`La altura redondeada hacia arriba es: ${alturaMetrosUp}`); // Imprimimos su resultado

// Creamos una variable que contendrá la altura redondeada hacia abajo
let pesoKilogramosDown = Math.floor(pesoKilogramos);
console.log(`El peso redondeado hacia abajo es: ${pesoKilogramosDown}`); // Imprimimos su resultado

// Creamos otra variable para obtener el máximo valor en JavaScript +1
let max_valor_JS_iguales = Number.MAX_VALUE + 1 === Number.MAX_VALUE; // Aquí calculamos si el valor máximo de JS + 1 es igual al valor máximo de JS
console.log(`El valor máximo de JS + 1 es igual al valor máximo de JS?: ${max_valor_JS_iguales}`);
