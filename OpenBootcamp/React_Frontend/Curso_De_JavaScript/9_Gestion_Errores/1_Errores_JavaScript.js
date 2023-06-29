const miFuncion = val => {
    if (typeof val === "number") return 2 * val;
    // return false;
    throw new Error("El valor debe ser de tipo numérico");
};

// const elDoble = miFuncion("Ala");
const numero = "8";

try {
    // Código que puede fallar
    console.log("Está ejecutándose de manera correcta");
    const doble = miFuncion(numero);
    console.log(doble);
} catch (e) {
    // En caso de fallar, quiero que ejecutes
    console.error(e);
    console.error("ERROR!!!");
} finally {
    console.log("Esto se va a ejecutar tanto si se produce algún error, como si no");
}

// InternalError, SyntaxError, TypeError, RangeError y ReferenceError
// https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Error
