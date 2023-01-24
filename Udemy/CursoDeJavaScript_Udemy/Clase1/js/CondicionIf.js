let numero = prompt("Dime un número entero");
numero = parseInt(numero);

if (numero > 0) {
    document.write(numero + " es mayor que cero.");
} else if (numero < 0) {
    document.write(numero + " es menor que cero.");
} else {
    document.write(numero + " es igual a cero");
}
