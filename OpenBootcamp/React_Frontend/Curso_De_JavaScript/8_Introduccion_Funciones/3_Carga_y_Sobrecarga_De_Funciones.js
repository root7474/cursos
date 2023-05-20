// Carga y sobrecarga de funciones
function hola() {
    console.log("Hola, soy la función 'hola()'");
}

function saludar() {
    hola();
}

saludar();

// 1.) Cargar función global()
// 2.) Añade saludar() por encima de la función global()
// 3.) Llamar a la función hola(): hola(), saludar(), global()
// 4.) se quita la función hola(): saludar(), global()
// 5.) Sale de la función saludar(): global()

// Stack Overflow
/* function recursiva() {
    recursiva();
}

recursiva(); */
