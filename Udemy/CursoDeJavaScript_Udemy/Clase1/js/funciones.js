// Funcionessin parametros y sin retornos de valor
function mostrar() {
    document.write("Hola desde la función<br/>");
}

for (let i = 0; i < 10; i++) {
    mostrar();
}

// Función con parametros
function imprimir(nombre) {
    document.write(`Hola ${nombre}<br/>`);
}

imprimir("David");
imprimir("Maritza");

// Función que devuelve un resultado
function mayor(val_1, val_2) {
    let resultado;

    if (val_1 > val_2) {
        resultado = val_1;
    } else {
        resultado = val_2;
    }

    return resultado;
}

document.write(mayor(4, 56));
let numeroMayor = mayor(4, 8);
document.write(`<br/>El número mayor es: ${numeroMayor}`);
