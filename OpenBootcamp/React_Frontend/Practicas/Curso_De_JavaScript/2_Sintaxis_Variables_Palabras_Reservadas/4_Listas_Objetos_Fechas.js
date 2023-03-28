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
const telefono = {
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
}

telefono.año = 2023;
telefono.marca = "Huawei";
console.log(telefono.marca);

// Fechas
// Librerías de apoyo: Moment.js
const ahora = new Date();
console.log(ahora);

const fechaMillis = new Date(10);
console.log(fechaMillis);

const fechaCadena = new Date("March 27 2023");
console.log(fechaCadena);

const fechaValores = new Date(2023, 2, 27);
console.log(fechaValores);

const día = ahora.getDate();
const mes = ahora.getMonth() + 1;
const año = ahora.getFullYear();
console.log(día, mes, año);
