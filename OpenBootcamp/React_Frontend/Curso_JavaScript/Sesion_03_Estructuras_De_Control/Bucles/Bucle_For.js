// Bucle For
for (let i = 0; i < 10; i++) {
    console.log(i);
}

let lista = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12];
for (let i = 0; i < lista.length; i++) {
    console.log(lista[i]);
}

// Estructura For...of
for (const valor of lista) {
    console.log(valor);
}

// Estructura forEch
lista.forEach(valor => {
    console.log(valor);
});

// Estructura for...in
let persona = {
    nombre: "David",
    apellido: "Rodríguez",
    edad: 26,
    isDeveloper: true
}

console.log(persona.nombre);

let prop = "edad";
console.log(persona[prop]);

for (let propiedad in persona) {
    console.log(propiedad);
    console.log(persona[propiedad]);
}
