// Listas, arrays, arreglos o vectores
const lista_1 = [1, "Hola", true, undefined, null];
const lista_2 = new Array(2, "Hola", true, undefined, null);
const lista_3 = new Array(3);
lista_3[0] = "Soy el primer elemento, index 0";
const lista_4 = [lista_1, lista_2, lista_3]

console.log(lista_1);
console.log(lista_2);
console.log(lista_3);
console.log(lista_4);

// Objetos
const movil = {
    altura: 10,
    anchura: 5,
    marca: "Xiaomi",
    isWhite: false,
    contactos: ["David", "Pipe", "Patricia"],

    tarjeta: {
        marca: "Sandisk",
        almacenamiento: 128,
    },

    "altura-tarjeta": 4,
};

movil.año = 2023;
movil.marca = "Samsung";

console.log(movil.marca);

// Fechas
// Librerías de apoyo: Moment.js
const ahora = new Date();
console.log(ahora);

const fecha_millis = new Date(10);
console.log(fecha_millis);

const fecha_cadena = new Date("March 25 2020");
console.log(fecha_cadena);

const fecha_valores = new Date(2022, 0, 15);
console.log(fecha_valores);

const dia = ahora.getDate();
const mes = ahora.getMonth() + 1;
const año = ahora.getFullYear();

console.log(dia, mes, año);
