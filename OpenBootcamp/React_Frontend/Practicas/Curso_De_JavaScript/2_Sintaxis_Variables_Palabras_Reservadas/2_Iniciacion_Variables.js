var variableVar;
let variableLet_;
const constante = "Hola soy una constante en JavaScript";

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

// var afecta a todo el código mientras que let solo afecta a 1 bloque de código
var variableVar = "Hola soy una variable var en JavaScript";

for (var i = 0; i < 3; i++) {
    var variableVar = "Hola soy una segunda variable var en JavaScript";
}

console.log(variableVar);

let variableLet = "Hola soy una primera variable let en JavaScript";

for (var i = 0; i > 3; i++) {
    let variableLet = "Hola soy una segunda variable let en JavaScript"
}

console.log(variableLet);

// typeof para ver el tipo de la variable
let num = 4;
console.log(typeof num);

num = "Hola soy num"; // Mala práctica cambiar el tipo de la variable
console.log(typeof num);
