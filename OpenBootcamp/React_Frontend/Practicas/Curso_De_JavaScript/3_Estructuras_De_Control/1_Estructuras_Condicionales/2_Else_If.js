// if else + if else
// Declaramos un variable nota
let nota = 5;

if (nota === 5) {
    console.log("Enhorabuena, has obtenido un sobresaliente"); // Esto se ejecutará si nota vale 5
} else if (nota === 4) {
    console.log("Buen trabajo pero podrías haberlo hecho mejor"); // Esto se ejecutará si nota vale 4
} else if (nota === 3) {
    console.log("Has obtenido un suficiente"); // Esto se ejecutará si nota vale 3
} else if (nota === 2) {
    console.log("No has aprobado por poco"); // Esto se ejecutará si nota vale 2
} else if (nota === 1) {
    console.log("No has estudiado nada, trabaja un poquito más para la próxima"); // Esto se ejecutará si nota vale 1
} else {
    console.log("Error!!!... Introduce una nota entre el 1 y el 5"); // Esto se ejecutará si no se ingresa una nota entre 1 y 5
}
