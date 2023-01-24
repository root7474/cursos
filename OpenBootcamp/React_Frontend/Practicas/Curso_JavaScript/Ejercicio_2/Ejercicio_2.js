// Autor: David Rodríguez

const nombre = "David";
const edad = 26
const eres_desarrollador = true;
const fecha_nacimiento = new Date(1996, 1, 5);
/* const fecha_libro = new Date();

fecha_libro.setFullYear(2016);
fecha_libro.setMonth(9); */

const libro_favorito = {
    titulo: "Python 3, Curso Práctico",
    autor: "Alberto Cuevas Álvarez",
    fecha: new Date(2016, 9, 14),
    
    /* fecha: {
        "año": fecha_libro.getFullYear(),
        "mes": fecha_libro.getMonth() + 1
    }, */
    
    url: "https://www.ra-ma.es/libro/python-3-curso-practico_47900/"
}

const datos_personales = [`Nombre: ${nombre}`, `Edad: ${edad}`, `Eres desarrollador?: ${eres_desarrollador}`, `Fecha de nacimiento: ${fecha_nacimiento}}`, 
                          `Libro favorito: {Título: ${libro_favorito.titulo}, Autor: ${libro_favorito.autor}, Fecha: ${libro_favorito.fecha}, url: ${libro_favorito.url}}`]

console.log(datos_personales);
console.log(libro_favorito);
