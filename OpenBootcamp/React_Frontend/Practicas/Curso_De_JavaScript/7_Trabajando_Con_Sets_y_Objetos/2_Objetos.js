// Trabajando con objetos
const obj = {
    id: 4,
    nombre: "David",
    apellido: "Rodríguez",
    isDeveloper: true,
    libros_favoritos: ["El método", "El código de la manifestación"],
    "4-juegos": [1, 2, 3, 4]
}

console.log(obj.id);
console.log(obj["4-juegos"]);

const prop = "isDeveloper";
console.log(obj[prop]);

const obj2 = obj;
console.log(obj2);

obj2.nombre = "Andrés";
console.log(obj2.nombre);
console.log(obj.nombre);

let val1 = 4;
let val2 = val1;

val2 = 7;
console.log(val1);
console.log(val2);

const obj3 = {...obj}
console.log(obj.nombre);
console.log(obj3.nombre);

// Cómo ordenar listas de objetos en función de una propiedad
const listaPeliculas = [
    {titulo: "Lo que el viento se llevó", año: 1939},
    {titulo: "Titanic", año: 1997},
    {titulo: "Mohana", año: 2016},
    {titulo: "El efecto mariposa", año: 2004},
    {titulo: "TED", año: 2012}
]

console.log(listaPeliculas);

// sort() -> MUTA EL VALOR DE LISTA ORIGINAL
listaPeliculas.sort((a, b) => a.año - b.año);
console.log(listaPeliculas);
