/* console.log("Indica el número de opción");
console.log("\n1.) Cargar");
console.log("\n2.) Imprimir");
console.log("\n3.) Salir\n"); */

/* document.write("Indica el número de opción" +
               "\n1.) Cargar." +
               "\n2.) Imprimir." +
               "\n3.) Salir\n"); */

opcion = parseFloat(prompt("Indica el número de opción" +
                           "\n1.) Cargar." +
                           "\n2.) Imprimir." +
                           "\n3.) Salir\n" +
                           "\nDame una opción: "));

switch (opcion) {
    case 1:
        document.write("Cargando ...");
        break;

    case 2:
        document.write("Imprimiendo ...");
        break;

    case 3:
        document.write("Saliendo ...");
        break;

    default:
        document.write("\nSelección no valida, introduce una opción correcta");
        break;
}
