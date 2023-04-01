// Operadores
const pi = 3.1415;
let num1 = 2 * pi;
let num2 = 4 / pi;

let resultado = num1 * num2;

document.write("El número pi es: " + pi);
document.write("<br/>El operador <strong>uno</strong> es: " + num1);
document.write("<br/>El operador <strong>dos</strong> es: " + num2);
document.write("<br/>El <strong>resultado</strong> es: " + resultado + "<br/>");

// Otra forma de incluir una variable dentro de una cadena
let nombre = "David";
document.write(`Aquí está la variable ${nombre} y la pongo en el lugar que quiero <br/>`);
document.write("Aquí está la variable ${nombre} y la pongo en el lugar que quiero");
