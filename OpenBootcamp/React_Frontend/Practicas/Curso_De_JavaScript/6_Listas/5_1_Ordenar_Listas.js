// sort()
const array_1 = [2, 5, 9, 15, 1, 2, 4];
console.log(array_1);

array_1.sort((a, b) => {
    if (a < b) {
        return -1;
    } else if (a > b) {
        return +1;
    } else {
        return a;
    }
});

console.log(array_1);

// Ordenar unicamente arrays numéricos
const arraysNumericos = [4, 1, 7, 3, 1, 3, 56, 1, 546];
arraysNumericos.sort((a, b) => b - a);
console.log(arraysNumericos);

// Interesante en arrays de objetos
const listaObjetos = [
    {nombre: "David", edad: 27},
    {nombre: "Patricia", edad: 50},
    {nombre: "Felipe", edad: 21},
    {nombre: "Andrés", edad: 27},
];

/* listaObjetos.sort((a, b) => {
    if (a.edad < b.edad) {
        return -1;
    } else if (a.edad > b.edad) {
        return +1;
    } else {
        return 0;
    }
}); */

listaObjetos.sort((a, b) => b.edad - a.edad);
console.log(listaObjetos);
