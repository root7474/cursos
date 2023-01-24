// Repetición for
let tabla = parseInt(prompt("Qué tabla quieres que calcule?: "));
document.write(`Empezamos con la tabla del ${tabla}:<br/><br/>`);

let i = 1;

// Repeticón con while
/* while (i <= 10) {
    resultado = tabla * i;
    document.write(`${tabla} * ${i} = ${resultado}<br/>`);
    i++;
}

document.write("Termina el bucle while <br/>") */

// Repetición con do while
do {
    resultado = tabla * i;
    document.write(`${tabla} * ${i} = ${resultado}<br/>`);
    i++;
} while (i <= 10);

document.write("Termina el bucle do while <br/>")
