let numero = prompt("Digita un número: ");
numero = parseInt(numero);

if (numero < 0) {
    document.write(`${numero} es menor que 0`);
} else if (numero > 0) {
    document.write(`${numero} es mayor que 0`);
} else if (numero == 0) {
    document.write(`${numero} es igual a 0`);
}
