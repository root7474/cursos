// Strings o cadenas de caracteres
let string_sng = 'Hola soy un texto con comillas simples';
let string_dbl = "Hola soy un texto con comillas dobles";

console.log(string_sng);
console.log(string_dbl);

let str_comillas_dobles_1 = "El otro día me dijo literalmente \"ve a sacar la basura\"";
let str_comillas_simples_1 = 'El otro día me dijo literalmente "ve a sacar la basura"';
let str_comillas_dobles_2 = "El otro día me dijo literalmente 've a sacar la basura'";
let str_comillas_simples_2 = 'El otro día me dijo literalmente \'ve a sacar la basura\'';

console.log(str_comillas_dobles_1);
console.log(str_comillas_simples_1);
console.log(str_comillas_dobles_2);
console.log(str_comillas_simples_2);

// Comillas invertidas (backticks)
let str_backticks = `Hola esto es un string con backsticks`;
console.log(str_backticks);

let nombre = "David";
console.log(`Hola ${nombre}, bienvenido`);

// Plantillas HTML
let plantilla = `
<html>
    <h1>Página web de ${nombre}</h1>
</html>
`;

console.log(plantilla);

// Introducción de variables en HTML
let libros = ["Empieza por el por qué", "El monje que vendió su Ferrari", "El poder del ahora"];
