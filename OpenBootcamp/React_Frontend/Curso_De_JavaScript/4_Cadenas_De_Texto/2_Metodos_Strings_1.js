// Métodos más utilizados con cadena de caracteres (parte 1)
// Cómo obtener la longitud de un string
let str = "Hola soy un string";
console.log(str.length);

// Obtener partes de cadenas de caracteres
// slice(), substring() y substr() (Deprecated)
let slice_str = str.slice(5, 10);
console.log(slice_str);

let substring_str = str.substring(5, 10);
console.log(substring_str);

let substr_str = str.substr(5, 10);
console.log(substr_str);

// Al utilizar strings, sólo reempleza la primera instancia
let cadena = "Hola mi nombre es David";
console.log(cadena);
console.log(cadena.replace("David", "Andrés"));

let texto_largo = "Tito no es un mono cualquiera. A Tito no le gusta trepar por los árboles y odia comer plátanos. Él prefiere pasear por el bosque, oler las flores y recoger las nueces que se caen de los árboles.";
console.log(texto_largo.replace("los", "cinco"));

// Al utilizar la expresión regular /g (global), reemplaza todas las instancias
console.log(texto_largo.replace(/los/g, "cinco"));
