// Repetición for
let tabla = parseInt(prompt("Qué tabla quieres que calcule?: "));
document.write(`Empezamos con la tabla del ${tabla}:<br/><br/>`);

for (let i = 1; i <= 10; i++) {
    resultado = tabla * i;

    // Saltar cuando i = 3
    /* if (i == 3) {
        continue;
    } */

    document.write(`${tabla} * ${i} = ${resultado}<br/>`);
}
