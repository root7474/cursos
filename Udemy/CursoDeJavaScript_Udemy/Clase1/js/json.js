const alumno = {
    nombre: "David",
    nota: 10
};

console.log(alumno);

alumno["nota"] = 5;
console.log(alumno);
console.log(alumno["nombre"] + " " + alumno.nota);

// Estructura compleja JSON
const alumnos = [
    {
        nombre: "David",
        nota: 10
    },

    {
        nombre: "Juana",
        nota: 10
    },

    {
        nombre: "Felipe",
        nota: 9.5
    }
];

console.log(alumnos);

let alumnaNueva = {
    nombre: "Maritza",
    nota: 10
};

alumnos.push(alumnaNueva);

// Recorrer JSON
for (let i = 0; i < alumnos.length; i++) {
    console.log(`${alumnos[i].nombre}`);
    document.write(`${alumnos[i].nombre}<br/>`);
}

console.log(alumnos);

alumnos.splice(1, 1);
console.log(alumnos);
