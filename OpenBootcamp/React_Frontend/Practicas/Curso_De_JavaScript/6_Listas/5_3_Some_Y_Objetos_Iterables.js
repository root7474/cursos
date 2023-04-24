// some()
const array_1 = [3, 7, 2, 4, 7, 9, 42, 35, 7865, 23, -2];
const res = array_1.some(valor => valor < 0);
console.log(res);

const existe = array_1.some(valor => valor === 9);
console.log(existe);

const listaObjetos = [
    {nombre: "David", edad: 27},
    {nombre: "Patricia", edad: 50},
    {nombre: "Felipe", edad: 21},
    {nombre: "Andrés", edad: 27},
];

const existeDavid = listaObjetos.some(persona => persona.nombre === "David");
console.log(existeDavid);

// Cómo obtener una lista a partir de un objeto iterable
const str = "Hola soy David";
console.log(str[5]);

const ar_str = Array.from(str);
console.log(ar_str);

// set()
const set = new Set([2, 3, "Hola", 4]);
const ar_set = Array.from(set);
console.log(ar_set);

// keys()
const keys = array_1.keys();
console.log(keys);

const ar_keys = Array.from(keys);
console.log(ar_keys);
