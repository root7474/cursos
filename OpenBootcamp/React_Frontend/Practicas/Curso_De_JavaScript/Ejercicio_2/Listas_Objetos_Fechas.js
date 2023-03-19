// Ejercicio de listas, objetos y fechas en JavaScript
// Autor: David Rodríguez

// Declaramos los datos que va a contener nuestra lista
let nombre = "David";
let edad = 27;
let eresDesarrollador = true;

// Declaramos variables con los respectivos datos de nuestra fecha de nacimiento
let fechaNacimiento = new Date();
let diaNacimiento = fechaNacimiento.setDate(5);
let mesNacimiento = fechaNacimiento.setMonth(1);
let añoNacimiento = fechaNacimiento.setFullYear(1996);

let nuevaFechaNacimiento = new Date(añoNacimiento)

// Declaramos un objeto loibroFavorito con los atributos de título, autor, fecha y url
let libroFavorito = {
    titulo: "Python 3 Curso Práctico",
    autor: "Alberto Cuevas Alvarez",
    fechaLibro: new Date(2016, 10, 14),

    url: "https://www.ra-ma.es/libro/python-3-curso-practico_47900/",
};

// Declaramos la lista
let datosLibroFavorito = "Libro favorito: " + libroFavorito.titulo + 
                         ", " + libroFavorito.autor + 
                         ", " + libroFavorito.fechaLibro;

let misDatos = [nombre, edad, eresDesarrollador, datosLibroFavorito]
console.log(misDatos);
