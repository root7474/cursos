const logger = require("./logger")
let numero = 4;

const miFuncion = valor => {
    if (typeof valor === "number") return 2 * valor;
    throw new Error("El valor debe ser numérico");
}

try {
    console.log(`Resultado: ${miFuncion(numero)}`);
} catch (e) {
    logger.error("ERROR!!!");
}
