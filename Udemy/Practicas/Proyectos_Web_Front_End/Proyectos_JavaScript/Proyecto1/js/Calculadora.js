class Matriz {
    constructor(matriz_1, matriz_2, matriz_3) {
        this._matriz_1 = matriz_1;
        this._matriz_2 = matriz_2;
        this._matriz_3 = matriz_3;
    }

    get matriz_1() {
        return this._matriz_1;
    }

    get matriz_2() {
        return this._matriz_2;
    }

    get matriz_3() {
        return this._matriz_3;
    }
}

class OperacionesMatricez extends Matriz {
    constructor(matriz_1, matriz_2, matriz_3, filas, columnas) {
        super(matriz_1, matriz_2, matriz_3);
        this._filas = filas;
        this._columnas = columnas;
    }

    get Filas() {
        return this._filas;
    }

    get Columnas() {
        return this._columnas;
    }
}

let filas = parseInt(prompt());
let columnas = parseInt(prompt());
let matriz_1 = [];
let matriz_2 = [];
let matriz_3 = [];
let numero;

function SumaMatricez() {
    matriz_1 = new Array(filas, columnas);
    matriz_2 = new Array(filas, columnas);
    matriz_3 = new Array(filas, columnas);

    for (let i = 0; i < filas; i++) {
        for (let a = 0; a < columnas; a++) {
            numero = parseInt(prompt());
            matriz_1[i, a] = numero;
        }
    }

    for (let i = 0; i < filas; i++) {
        for (let a = 0; a < columnas; a++) {
            numero = parseInt(prompt());
            matriz_2[i, a] = numero;
        }
    }
    
    for (let i = 0; i < filas; i++) {
        for (let a = 0; a < columnas; a++) {
            matriz_3[i, a] = matriz_1[i, a] + matriz_2[i, a];
        }
    }

    /* this._matriz_1 = matriz_1;
    this._matriz_2 = matriz_2;
    this._matriz_3 = matriz_3; */

    return(filas, columnas, matriz_1, matriz_2, matriz_3);
}

function MostrarResultado() {
    console.log("Matriz 1");
    document.write("</br>Matriz 1: </br>")

    for (let i = 0; i < filas; i++) {
        console.log("\n[");
        document.write("</br> [");

        for (let a = 0; a < columnas; a++) {
            console.log(matriz_1[i, a]);
            document.write(matriz_1[i, a]);
        }
        
        console.log("]");
        document.write("]");
    }

    console.log("Matriz 2");
    document.write("</br></br>Matriz 2: </br>")

    for (let i = 0; i < filas; i++) {
        console.log("\n[");
        document.write("</br> [");

        for (let a = 0; a < columnas; a++) {
            console.log(matriz_2[i, a]);
            document.write(matriz_2[i, a]);
        }
        
        console.log("]");
        document.write("]");
    }

    console.log("Matriz 3");
    document.write("</br></br>Matriz 3: </br>")

    for (let i = 0; i < filas; i++) {
        console.log("\n[");
        document.write("</br> [");

        for (let a = 0; a < columnas; a++) {
            console.log(matriz_3[i, a]);
            document.write(matriz_3[i, a]);
        }
        
        console.log("]");
        document.write("]");
    }

    filas = filas;
    columnas = columnas;
    return (filas, columnas);
}

let operaciones = new OperacionesMatricez(matriz_1, matriz_2, matriz_3, filas, columnas);
SumaMatricez();
MostrarResultado();

// let imprimirMatriz = operaciones.SumaMatricez(2, 2);
