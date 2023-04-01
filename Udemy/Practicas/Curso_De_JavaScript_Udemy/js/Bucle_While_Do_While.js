let tabla_multiplicar = parseInt(prompt("Qué tabla quieres que calcule?: "));
document.write(`Empezamos con la tabla del ${tabla_multiplicar}:<br/><br/>`);

let i = 1;

// Bucle while
/* while (i <= 10) {
    resultado = tabla_multiplicar * i;
    document.write(`${tabla_multiplicar} X ${i} = ${resultado}<br/>`);

    i++;
}

document.write("<br/>Termina el bucle while."); */

// Bucle Do While
do {
    resultado = tabla_multiplicar * i;
    document.write(`${tabla_multiplicar} X ${i} = ${resultado}<br/>`);

    i++;
} while (i <= 10);

document.write(`<br/>Termina el bucle Do While.`)
