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
const arrayNumericos = [4, 1, 7, 3, 1, 3, 56, 1, 546];
arrayNumericos.sort((a, b) => b - a);
console.log(arrayNumericos);

// Interesante en arrays de objetos
const listaObjetos = [
    {nombre: "Leire", edad: 35},
    {nombre: "Gorka", edad: 34},
    {nombre: "Miguel", edad: 28},
    {nombre: "Lucía", edad: 3},
    {nombre: "Amaia", edad: 29},
]

/* listaObjetos.sort((a, b) => {
    if (a.edad < b.edad) {
        return -1;
    } else if (a.edad > b.edad) {
        return +1;
    } else {
        return 0;
    }
}); */

listaObjetos.sort((a, b) => a.edad - b.edad);
console.log(listaObjetos);
