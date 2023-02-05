// Declaramos una función llamada primerNombre()
function primerNombre() {
    var nombre = "David"; // Declaramos una variable con un valor de tipo string
    {
        var nombre = "Andrés"; // Declaramos la misma variable pero con distinto valor
        console.log(nombre);
    }

    console.log(nombre);
}

// Declaramos otra función llamada segundoNombre()
function segundoNombre() {
    let nombre = "Andrés"; // Declaramos una variable con un valor de tipo string
    {
        let nombre = "David"; // Declaramos la misma variable pero con distinto valor
        console.log(nombre);
    }

    console.log(nombre);
}

primerNombre();
segundoNombre();
