// Cómo obtener una lista a partir de otra slice()
const array_1 = ["Hola", 1, 2, 3, true, null, "Adiós"];

// NO MODIFICA EL VALOR DEL ARRAY ORIGINAL
console.log(array_1.slice(1, 4));

const array_2 = array_1.slice(2, 5);
console.log(array_2);

const array_3 = array_1.slice(2, -2);
console.log(array_3);
