// Iterar valores de una lista
const array_1 = ["Hola", 2, 5, 90, false, undefined];

// Forma antigua y poco eficiente
for (let i = 0; i < array_1.length; i++) {
    console.log(array_1[i]);
}

// Forma ES6 (más eficiente) forEach()
let suma = 0;
const arrayNums = [3, 6, 2, 77, 2, 3, 93, 19];

arrayNums.forEach(valor => {
    suma += valor;
    console.log(valor);
});

console.log(suma);

// Búsqueda de un valor dentro de una lista find()
// Quiero encontrar el elemento 90
const variable = array_1.find(valor => {
    if (valor === 90) {
        return true;
    }
});

console.log(variable);

const listaObjetos = [
    {nombre: "David", apellido: "Rodríguez"},
    {nombre: "Patricia", apellido: "Bolaños"},
    {nombre: "Felipe", apellido: "Rodríguez"},
    {nombre: "Andrés", apellido: "Bolaños"},
];

/* const objeto = listaObjetos.find(o => {
    if (o.nombre === "Felipe") return true;
});

console.log(objeto); */

const objeto = listaObjetos.find(o => o.nombre === "Felipe");
console.log(objeto.apellido);

const {apellido} = listaObjetos.find(o => o.nombre === "Felipe");
console.log(apellido);
