class coche {
    // Constructor
    constructor(marca, motor, color) {
        this.marca = marca;
        this.motor = motor;
        this._color = color;
        this._velocidad = 0;
    }

    // Atributos
    get velocidad() {
        return this._velocidad
    }

    set cambiaColor(color) {
        this._color = color;
    }

    get dameDatos() {
        return `El coche ${this.marca} es de color ${this._color}`;
    }

    // Metodos (sin poner la palabra function)
    arrancar() {
        console.log("Arrancado");
    }

    parar() {
        console.log("Parado");
    }

    acelerar() {
        this._velocidad = this._velocidad + 10;
        console.log(`Velocidad actual: ${this._velocidad}`);
    }

    frenar() {
        if (this._velocidad > 0) {
            this._velocidad = this._velocidad - 10;
            console.log(`Velocidad actual: ${this._velocidad}`);
        } else {
            this._velocidad = 0;
            console.log(`Velocidad actual: ${this._velocidad}`);
        }
    }
}

const miCoche = new coche("Seat", "eléctrico", "verde");
console.log(miCoche.dameDatos);
miCoche.arrancar();
miCoche.acelerar();
miCoche.acelerar();
console.log(`La velocidad actual es de: ${miCoche.velocidad}`);
miCoche.frenar();
console.log(`La velocidad actual es de: ${miCoche.velocidad}`);
console.log(miCoche.dameDatos);
miCoche.parar();
