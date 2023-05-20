// Funciones de tipo flecha - funciones anónimas
const array = [1, 5, 6, 7, 12, 8, 92];
const array2 = array.map(valor => valor * 2);

console.log(array2);

//Hoisting
console.log(doble(6));

// Las funciones de tipo flchea debe ser inicializadas para poder acceder a ellas
const dobleDelValor = valor => valor * 2;
console.log(dobleDelValor(6));

const array3 = array.map(dobleDelValor);
console.log(array3);

function doble(valor) {
    return valor * 2;
}

