// Comparaciones
// Igualdad débil
if (5 == 5) {
    console.log("5 es igual a 5");
}

// Igualdad fuerte
if (5 === 5) {
    console.log("5 es muy igual a 5");
}

let a = 5;
console.log(typeof a);

let b = "5";
console.log(typeof b);

// == sólo compara el valor
// === compara el valor y el tipo

if (a == b) {
    console.log("a es igual a b - Débil");
}

if (a === b) {
    console.log("a es igual a b - Fuerte");
} else {
    console.log("a no es igual que b");
}

// Desigualdad
let c = 4;
let d = "4";

if (c != d) {
    console.log("c es diferente de d - Débil");
}

if (c !== d) {
    console.log("c es diferente de d - Fuerte");
} else {
    console.log("c es igual que d");
}

// Comparaciones mayor que y menor que
let max = 10;
let min = 5;

if (max > min) {
    console.log("max es mayor que min");
}

if (max >= 10) {
    console.log("max es mayor o igual que min");
}

if (min < max) {
    console.log("min es menor que max");
}

if (min <= max) {
    console.log("min es menor o igual que max");
}
