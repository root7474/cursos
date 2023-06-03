// Calculadora de rrays 2D
// Autor: David Rodríguez
function sumaArrays(tamañoArray) {
    const matriz1 = new Array(tamañoArray);
    const matriz2 = new Array(tamañoArray);
    const sumaMatricez = new Array(tamañoArray);
    let elementosMatricez;
    
    for (let i = 0; i < tamañoArray; i++) sumaMatricez[i] = new Array(tamañoArray);

    elementosMatricez = sumaMatricez.map((valor) => {
        const suma = new Array(tamañoArray);

        for (let i = 0; i < valor.length; i++) {
            matriz1[i] = i + 1;
            matriz2[i] = i + 1;
            suma[i] = matriz1[i] + matriz2[i];
        }

        return suma;
    });

    return elementosMatricez;
}

let tamañoArray = 4;
console.log(sumaArrays(tamañoArray));
