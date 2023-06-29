function suma(a, b) {
    return a + b;
}

function multiplica(a, b) {
    return a * b;
}

function eleva(a, b) {
    return a ** b;
}

function factorial(a) {
    // Factorial de 5: 5 x 4 x 3 x 2 x 1
    let factorial = 1;
    for (let i = 1; i <= a; i++) factorial *= i;
    
    return factorial;
}

module.exports = {
    suma,
    multiplica,
    eleva,
    factorial
}
