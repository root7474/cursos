// Break t continue
// Labels
let unidades = 0;
let decenas = 0;

bucleDecenas: while (true) {
    bucleUnidades: while (true) {
        console.log(`El número actual es: ${decenas}${unidades}`);
        unidades++;

        if (unidades === 10) {
            unidades = 0;
            break bucleUnidades;
        }

        if (decenas === 2) {
            decenas = 0;
            break bucleDecenas;
        }
    }

    decenas++;
}

console.log("Hemos terminado");
