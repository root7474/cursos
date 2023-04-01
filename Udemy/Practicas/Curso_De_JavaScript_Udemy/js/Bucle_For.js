let tabla_multiplicar = parseInt(prompt("Qué tabla quieres que calcule?: "));
document.write(`Tabla del ${tabla_multiplicar}: <br/><br/>`);

for (let i = 1; i <= 10; i++) {
    resultado = tabla_multiplicar * i;
    
    // Saltar cuando i sea igual a 3
    /* if (i == 3) {
        continue;
    } */

    document.write(`${tabla_multiplicar} X ${i} = ${resultado} <br/>`)
}
