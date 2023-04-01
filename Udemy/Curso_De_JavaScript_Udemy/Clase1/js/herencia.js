class Persona {
    constructor(nombre, edad) {
        this._nombre = nombre;
        this._edad = edad;
    }

    get nombre() {
        return this._nombre;
    }

    get edad() {
        return this._edad;
    }

    info() {
        return `Me llamo ${this._nombre} y tengo ${this._edad} años`;
    }

    dormir() {
        console.log("Estoy durmiendo");
    }

    comer() {
        console.log("Estoy comiendo");
    }

    despertar() {
        console.log("Ya estoy despierto");
    }
}

class Trabajador extends Persona {
    constructor(nombre, edad, salario) {
        super(nombre, edad);
        this.trabaja = "estoy";
        this._salario = salario;
    }

    get salario() {
        return this._salario;
    }

    set salario(salario) {
        this._salario = salario;
    }

    info() {
        return `Me llamo ${this._nombre}, tengo ${this._edad} años, ` + 
                        `${this.trabaja} trabajando y gano $${this._salario} mensuales.`;
    }
}

const persona_1 = new Persona("David", 26);
console.log(persona_1.info());
persona_1.comer();
persona_1.dormir();
persona_1.despertar();

const trabajador = new Trabajador("Andrés", 26, 2500000)
console.log(trabajador.info());
