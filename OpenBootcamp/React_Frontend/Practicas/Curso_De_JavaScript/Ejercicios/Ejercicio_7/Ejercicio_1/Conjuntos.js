// Ejercicio 1. Conjuntos
// Autor: David Rodríguez

const arrayFamilia = ["Felipe", "Patricia", "David"]; // Declaramos un array con los nombres de los integrantes de nuestra familia
const setFamilia = new Set(arrayFamilia); // Creamos un set que contendrá al array que hemos creado

setFamilia.add("David"); // Agregamos un valor ya existente dentro del set
console.log("Les presento a mi familia y a un nuevo integrante ;)");

// Recorreamos a nuestro set con un forEach() 
setFamilia.forEach(element => {
    console.log(element); // Como veremos no imprime el valor que hemos duplicado
});

setFamilia.add("JavaScript") // Agregamos un nuevo elemento al set

// volvemos a recorrer a nuestro set con un forEach()
setFamilia.forEach(element => {
     // Aquí nos imprime todos los valores de nuestro set más el valor "JavaScript", a excepción del valor duplicado
    console.log(element); 
})
