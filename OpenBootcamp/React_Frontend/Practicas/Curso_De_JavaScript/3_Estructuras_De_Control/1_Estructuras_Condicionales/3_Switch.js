// Sentencias switch
let nota = 4; // Declaramos una variable nota

switch(nota) {
    case 5:
        console.log("nhora buena, has obtenido un sobresaliente"); // Esto se ejecuta en el caso de que la nota sea 5
        break;
    case 4:
        console.log("Buen trabajo pero podrías haberlo hecho mejor"); // Esto se ejecuta en el caso de que la nota sea 4
        break;
    case 3:
        console.log("No has aprobado por poco"); // Esto se ejecuta en el caso de que la nota sea 3
        break;
    case 2:
        console.log("No has aprobado por poco"); // Esto se ejecuta en el caso de que la nota sea 2
        break;
    case 1:
        console.log("No has estudiado nada, trabaja un poquito más para la próxima"); // Esto se ejecuta en el caso de que la nota sea 1
        break;
    default:
        console.log("Error!!!... Introduce una nota entre el 1 y el 5"); // Caso por defecto si la nota ingresada no está entre los valores de 1 y 5
        break;
}
