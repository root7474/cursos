// Comparaciones
// Igualdad débil
if (5 == 5) {
    console.log("5 es igual a 5");
}

// Igualdad fuerte
if (5 === 5) {
    console.log("5 es igual a 5");
}

// Declaramos variables a y b y miramos su tipo
let a = 5;
let b = "5";

console.log(typeof a);
console.log(typeof b);

// == -> Sólo compara su valor
// === -> Compara su valor y su tipo

if (a == b) {
    console.log(`${a} es igual que $ {b}`);
}

if (a === b) {
    console.log(`${a} es igual que $ {b}`);
} else {
    console.log(`${a} no es igual que ${b}`);
}

// Desigualdad
// Declaramos variables max y min
let max = 10;
let min = 5;

// Comparamos su valor
if (max > min) {
    console.log(`${max} es mayor que ${min}`); // Se ejecuta esto si max es mayor que min
}

if (max >= min) {
    console.log(`${max} es mayor o igual que ${min}`); // Se ejecuta esto si max es mayor o igual que min
}

if (min < max) {
    console.log(`${min} es menor que ${max}`); // Se ejecuta esto si min es menor que max
}

if (min <= max) {
    console.log(`${min} es menor o igual que ${max}`); // Se ejecuta esto si min es menor o igual que max
}
