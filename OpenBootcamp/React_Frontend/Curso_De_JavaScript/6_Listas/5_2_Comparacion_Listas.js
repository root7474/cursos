// Cómo podemos comparar listas
// every()
const array = [4, 6, 7, 8, 3, 6, 2, 1, -4, -7, 12, 5, -40];

/* const resultado = array.every(valor => {
    if (valor > 0) {
        return true;
    } else {
        return false;
    }
}); */

const resultado = array.every(valor => valor > 0);
console.log(resultado);

// Comparación de listas
const ar_1 = [1, 2, 3, 4];
const ar_2 = [1, 2, 3, 4];
console.log(ar_1 === ar_2);

const compararArrays = (array_1, array_2) => {
    if (array_1.length !== array_2.length) return false;
    const res = array_1.every((valor, i) => valor === array_2[i])
    return res
}

const ar_3 = [1, 2, 3, 9];
console.log(compararArrays(ar_1, array_2));
