var variable;
let variableLet_;
const constante = "Hola soy una constante";

var a = 1;
console.log(a);

a = 4;
console.log(a);

console.log(constante);

// constante = "Adiós"; // Nos dá un error

let b = 3;
console.log(b);

b = 5;
console.log(b);

// var afecta a todo el código y let solo afecta a un bloque de código
var variable = "Hola soy un a variable var";

for (var i = 0; i < 3; i++) {
    var variable = "Soy la segunda variable";
}

console.log(variable);

let variableLet = "Hola soy una variable let";

for (let index = 0; index < 3; index++) {
    let variableLet = "Soy la segunda variable let"; // Mala práctica volver a declarar la variable
}

console.log(variableLet);

// typeof para ver el tipo de la variable
let num = 4;
console.log(typeof num);

num = "Hola soy num"; // Mala práctica cambiar el tipo de la variable
console.log(typeof num);
