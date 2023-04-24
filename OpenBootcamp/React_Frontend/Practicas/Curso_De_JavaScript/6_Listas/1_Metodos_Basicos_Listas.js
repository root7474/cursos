// Cómo trabajar con listas (arrays, arreglos, vectores...)
let var_1 = {id: false};
let array = [1, "Hola", false, {id: 5}, null, undefined, var_1];
console.log(array);

// Acceder a los valores de un array a través de su posición
// array[indice] => 0, 1, 2, 3, 4, 5...
console.log(array[0]);
console.log(array[1]);
console.log(array[2]);
console.log(array[3]);

// Métodos para introducir nuevos valores en nuestros arrays
// push(), unshift() => Mutan el valor de un array

// Valores al final -> push()
array.push("Final", 45, 100, false);
console.log(array);

// Valores al principio -> unshift()
array.unshift("Inicio", 87, 99);
console.log(array);

// Métodos para eliminar valores en nuestros arrays
// pop(), shift(), => Mutan el valor del array
const array_2 = [1, 3, "Hola", false];

// Valores al final -> pop()
array_2.pop();
console.log(array_2);

// Valores al principio -> shift()
array_2.shift();
console.log(array_2);

// Método para eliminar, modificar o añadir valores en nuestro array
// splice(x, y, z)
const array_3 = [1, 2, 3, 4, 5, 6];

// Eliminar valores -> splice(indice, numValoresAeliminar)
array_3.splice(2, 1);
console.log(array_3);

// Añadir valores -> splice(indice, 0, valores)
array_3.splice(2, 0, "Hola");
console.log(array_3);

// Modificar valores -> splice(indice, 1, valores)
array_3.splice(2, 1, 3);
console.log(array_3);
