// Qué son las funciones, cómo se declaran y cómo se utilizan
function saludar(nombre) {
    console.log(`Hola ${nombre}`);
}

// saludar("David");
const nom = "David"
saludar(nom);

///
function despedir(nombre) {
    nombre = "Diego"
    console.log(`Adiós ${nombre}`);
}

let nombre_2 = "Andrés";
console.log(nombre_2);

despedir(nombre_2);
console.log(nombre_2);

///
let persona = {nombre: "David", apellido: "Rodríguez"};
saludarPersona(persona);
console.log(persona);

function saludarPersona(objeto) {
    objeto.apellido = "Bolaños";
    console.log(`Hola ${objeto.nombre} ${objeto.apellido}`);
}

// Parámetros por defecto
function imprimeNumero(numero = 7) {
    console.log(numero);
}

imprimeNumero();

///
function imprimir(...parametros) {
    console.log(parametros);
}

imprimir(1, 3, 9, 2, "Hola", {id: 9});

///
function suma(...nums) {
    return nums.reduce((a, b) => a + b);
}

const s= suma(1, 2, 3, 4, 9, 15, 16);
console.log(s);

///
let variable = "Hola";

function multiplicar(a = 0, b = 0) {
    console.log(variable);
    return a * b;
}

console.log(multiplicar(4, 9));
