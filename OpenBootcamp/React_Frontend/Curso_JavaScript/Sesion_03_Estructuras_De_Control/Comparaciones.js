// Comparación de igualdad

let a = 5
let b = "5"

// == Solo compara el valor
// === Compara el valor y el tipo

if (a == b) {
    console.log("a es igual a b = Débil");
}

if (a === b) {
    console.log("a es igual a b = Fuerte");
}

// Desigualdad
let c = 4;
let d = "4";

if (c != d) {
    console.log("c es diferebnte de d = Débil");
}

if (c !== d) {
    console.log("c es diferebnte de d = Fuerte");
}

// Mayor que y menor que
let max = 10
let min = 5;

if (max > min) {
    console.log("Max es mayor que min");
}

if (max >= 10) {
    console.log("Max es mayor o igual que min");
}

if (min < max) {
    console.log("Min es menor que max");
}

if (min <= max) {
    console.log("Min es menor o igual que max");
}
