opcion = parseFloat(prompt("Digita una opción: \n" +
                         "\n1.) Cargar." +
                         "\n2.) Imprimir." +
                         "\n3.) Salir.\n" +
                         "\nOpcion: "));

switch(opcion) {
    case 1:
        document.write("Cargando...");
        break;

    case 2:
        document.write("Imprimiendo...");
        break;

    case 3:
        document.write("Saliendo...");
        break;

    default:
        document.write("\nOpción incorrecta!!!");
        break;
}
