// Importamos los módulos necesarios para este programa
import chalk from "chalk"; // Instalamos la librerí "chalk" con npm y la importamos
import {suma, multiplica} from "./operaciones/controller.js"; // Importamos las funciones del módulo "controller.js"

// Llamada a las funciones "suma()" y "multiplica()" y les pasamos sus respectivos parámetros
let resultadoSuma1 = suma(1, 2); // Hacemos la suma de "1 + 2" y guardamos su resultado
let resultadoSuma2 = suma(4, 5); // Hacemos la suma de "4 + 5" y guardamos su resultado
let resultadoMultiplica = multiplica(resultadoSuma1, resultadoSuma2); // Multiplicamos los resultados de ambas sumas

// Imprimimos por consola el resultado de las operaciones de suma y multiplicación
// Con la librebría "chalk" agregamos un estilo de color verde a la salida de la consola 
// Con "chalk.green.bold()" añadimos un estilo de color verde con negrita a la multiplicación
console.log(chalk.green(`1 + 2 = ${resultadoSuma1}` +
            `\n4 + 5 = ${resultadoSuma2}` +
            chalk.green.bold(`\n${resultadoSuma1} x ${resultadoSuma2} = ${resultadoMultiplica}`)));
