// Ejercicio 4
// Autor: David Rodríguez

// Creamos dos strings que contendrán el nombre y el apellido
let nombre = "David";
let apellido = "Rodríguez";

// Creamos otro string para concatenar el nombre y el apellido
let estudiante = `${nombre} ${apellido}`;
console.log(`Estudiante: ${estudiante}`); // Mostramos el resultado por consola

// Creamos otros dos strings que contenga el nombre y el apellido del estudiante en mayúsculas y en minúsculas
let estudianteMayus = estudiante.toUpperCase();
let estudianteMinus = estudiante.toLowerCase();

// Imprimimos los resultados en mayúsculas y en minúsculas
console.log(`Estudiante en mayúsculas: ${estudianteMayus}`);
console.log(`Estudiante en minúsculas: ${estudianteMinus}`);

// Creamos un avaraible que contiene todas las letras de la cadena "estudiante", incluídos los espacios
let estudianteLength = estudiante.length;
console.log(`Número de caracteres de ${estudiante}: ${estudianteLength}`); // Imprimimos el resultado por consola

// Creamos una variable con la primera letra del nombre y mostramos su resultado en consola
let nombre_2 = nombre.charAt(0);
console.log(`Primera letra del nombre ${nombre}: ${nombre_2}`);

// Creamos una variable con la última letra del apellido y mostramos su resultado en consola
let apellido_2 = apellido.charAt(apellido.length - 1);
console.log(`última letra del apellido ${apellido}: ${apellido_2}`);

// Creamos otro string que elimine los espacios de la cadena "estudiante"
let estudiante_2 = estudiante.replace(/ /g, "");
console.log(`${estudiante} sin espacios: ${estudiante_2}`);

// Creamos un último string para ver si el nombre está contenido dentro de la cadena estudiante
let nombreEstudiante = estudiante.includes(nombre);
console.log(`El nombre ${nombre} está dentro la cadena \"${estudiante}\"?: ${nombreEstudiante}`);
