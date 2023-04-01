const alumno = {
    nombre: "David",
    nota: 9.5,
};

console.log(alumno);

alumno["nota"] = 10;
console.log(alumno);
console.log(alumno["nombre"] + " " + alumno.nota);

const alumnos = [
    {
        nombre: "Viviana",
        nota: 9.5
    },

    {
        nombre: "David",
        nota: 10
    },

    {
        nombre: "Maritza",
        nota: 10
    }
];

console.log(alumnos);
let alumnaNueva = {
    nombre: "Lucia",
    nota: 9.9
};

alumnos.push(alumnaNueva);
console.log(alumnos);

// Recorrer JSON
for (let i = 0; i < alumnos.length; i++) {
    console.log(`${alumnos[i].nombre}`);
    document.write(`${alumnos[i].nombre}</br>`);
}

alumnos.splice(1, 1);
console.log(alumnos);
