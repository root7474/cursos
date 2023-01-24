const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let resultado;
let condicion;
let Valor;

console.log("Usando forEach: ");

numeros.forEach(function(numero) {
    resultado = numero * 2;
    console.log(resultado);
});

// Aplicar función a cada elemento del array - MAP
const duplica = numeros.map(function(numero) {
    resultado = numero * 2;
    return " " + resultado;
});

console.log("Usando MAP: " + duplica);

// Extraer elementos que cumplen una condición - FILTER
const mayores = numeros.filter(function(numero) {
    condicion = numero > 9;
    return condicion;
});

console.log("Usando FILTER: " + mayores);

// Devolver el indice del valor coincidente
const indice = numeros.findIndex(function(valor) {
    condicion = valor === 7;
    return condicion;
});

console.log("Coincide con el número 7 con el indice...\n" + indice);

// Devolver elemento coincidente
const elemento = numeros.find(function(numero) {
    condicion = numero == 10;
    return condicion;
});

console.log(`Valor ${elemento} encontrado`);

// Devolver cualquier elemento coincidente o devolver un error
try {
    const valor = numeros.find(function() {
        condicion = 10;

        for (const element of numeros) {
            if (condicion == element) return condicion;
        }
    });

    Valor = valor.valueOf.call(condicion);
    console.log(`Valor ${Valor} encontrado`);
} catch (error) {
    console.log(`Error!!!... valor ${condicion} no definido`);
}
