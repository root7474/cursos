// Ejercicio 2: Objetos
// Autor: David Rodríguez
// Creamos un objeto con nuestros datos personales
let datosPersonalesObjeto = {nombre: "David", apellido: "Rodríguez", edad: 27, altura: 1.65, eresDesarrollador: true};
let edad = datosPersonalesObjeto.edad; // Creamos una variable "edad" y guardamos lo que hay entro del atributo edad de nuestro objeto
console.log(edad); // Imprimimos lo que hay dentro de nuestra variable "edad"

// Creamos un a lista de datos personales y le agregamos el objeto que hemos creado
// Más otros objetos con datos personales de dos amigos
let listaDatosPersonas = [
    datosPersonalesObjeto,
    {nombre: "Maritza", apellido: "Hernández", edad: 29, altura: 1.50, esDesarrollador: true},
    {nombre: "Ricardo", apellido: "Taco", edad: 25, altura: 1.69, esDesarrollador: true},
];

// Creamos otra lista pero con con toda la información de datos personales ordenados por edad de mayor a menor
let listaOrdenadaPorEdad = listaDatosPersonas.sort((a, b) => b.edad - a.edad);
console.log(listaOrdenadaPorEdad); // Imprimimos el resultado por consola
