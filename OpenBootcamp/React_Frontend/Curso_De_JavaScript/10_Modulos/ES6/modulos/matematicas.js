export function suma(a, b) {
    return a + b;
}

export function multiplica(a, b) {
    return a * b;
}

export function eleva(a, b) {
    return a ** b;
}

export function factorial(a) {
    // Factorial de 5: 5 x 4 x 3 x 2 x 1
    let factorial = 1;
    for (let i = 1; i <= a; i++) factorial *= i;
    
    return factorial;
}

export const nombre = "Matemáticas";
