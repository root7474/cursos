// Bucles for
// i = i + 1;
// i += 1;
// i++;

for (let i = 0; i < 10; i++) {
    // ESto es el bucle
    console.log(i);
}

let lista = [1, 4, 6, 2, 3, 7, 10, 12, 800];

for (let i = 0; i < lista.length; i++) {
    console.log(lista[i] * 4);
}

// EStructura for ... of
for (let i of lista) {
    console.log(i);
}

// EStructura foreach()
lista.forEach(i => {
    console.log(i);
});

// Estructura for ... in
let persona = {
    nombre: "David",
    apellido: "Rodríguez",
    edad: 27,
    isDeveloper: true,
}

let propiedad = "edad";
console.log(persona[propiedad]);

for (let i in persona) {
    console.log(i + ": " + persona[i]);
}
