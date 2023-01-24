// Listas, array o arreglo
const lista1 = [1, "Hola", true, undefined, null];
const lista2 = new Array(2, "Hola", true, undefined, null);
const lista3 = new Array(3);

lista3[0] = "Soy el primer elemento, index 0";
const lista4 = [lista1, lista2, lista3];

console.log(lista1);
console.log(lista2);
console.log(lista3);
console.log(lista4);

// Objetos
const movil = {
    altura: 10,
    anchura: 5,
    marca: "Xiaomi",
    isWhite: false,
    contactos: ["David", "Patricia", "Felipe"],

    tarjeta: {
        marca: "Sandisk",
        almacenamiento: 64
    },

    "altura-tarjeta": 4
}

movil.year = 2022;
movil.marca = "Samsung";

console.log(movil.marca);

// Fechas
// Librerías de apoyo Moment.js
const ahora = new Date();
console.log(ahora);

const fecha_milis = new Date(10); // Utilizando milisegundos
console.log(fecha_milis);

const fecha_cadena = new Date("march 25 2020");
console.log(fecha_cadena);

const fecha_valores = new Date(2012, 0, 15);
console.log(fecha_valores);

const dia = ahora.getDate();
const mes = ahora.getMonth() + 1;
const year = ahora.getFullYear();

console.log(dia, mes, year);
