// Ejercicio #6
// Autor David Rodríguez
// Creamos una lista de compras
let listaCompras = ["Papas Margarita", "Frutiño", "Agua Brisa con gas", "Rizadas", "Gaseosa Cigarra Clásica"];
console.log(listaCompras); // Imprimimos por consola nuestra lista de compras

// Agregamos el producto "Aceite de Girasol" a nuestra lista
listaCompras.push("Aceite de Girasol");
console.log(listaCompras);

// Eliminamos el producto que hemos agregado
listaCompras.pop("Aceite girasol")
console.log(listaCompras);

// Creamos una segunda lista con 3 películas favoritas (objetos con propiedades: titulo, director, fecha)


let listaPeliculasFavoritas = [
    {titulo: "Perl Harbor", director: "Michael Bay", fecha: new Date(2001, 4, 25)},
    {titulo: "Ralph el Demoledor", director: "Rich Moore", fecha: new Date(2013, 0, 11)},
    {titulo: "La pasión de Cristo", director: "Mel Gibson", fecha: new Date(2004, 1, 25)},
]

console.log(listaPeliculasFavoritas); // Imprimimos por consola nuestra lista

// Creamos una tercera lista que contendrá las películas posteriores al 1 de enero de 2010
let listaPelisPosteriores = listaPeliculasFavoritas.filter(pelisPosteriores => pelisPosteriores.fecha > new Date(2010, 0, 1));
console.log(listaPelisPosteriores); // Imprimimos por consola nuestra nueva lista

// Creamos un cuarta lista con el nombre de los directores de la lista de películas
/* const listaNombresDirectores = listaPeliculasFavoritas.map((peliculas, indice) => {
    return `${indice + 1} - ${peliculas.director}`
}); */

let listaNombresDirectores = listaPeliculasFavoritas.map((nombresDirectores, indice) => `${indice + 1} - ${nombresDirectores.director}`);
console.log(listaNombresDirectores);

// Creamos una sexta lista con los títulos de la lista de películas original (utilizando map)
/* let listaTitulosPelis = listaPeliculasFavoritas.map((titulos, indice) => {
    return `${indice + 1} - ${titulos.titulo}`
}); */

let listaTitulosPelis = listaPeliculasFavoritas.map((titulos, indice) => `${indice + 1} - ${titulos.titulo}`);
console.log(listaTitulosPelis);

// La siguiente lista contendrá la lista de directores y también la listade títulos con el método "concat()"
let listaPelisConcat = listaNombresDirectores.concat(listaTitulosPelis);
console.log(listaPelisConcat);

// Creamos una última lista igual que la anterior, utilizando el factor de propagación
let listaPelisProp = [...listaNombresDirectores, ...listaTitulosPelis];
console.log(listaPelisProp);
