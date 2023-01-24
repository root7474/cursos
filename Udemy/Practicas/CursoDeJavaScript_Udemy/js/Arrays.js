// Crear ARRAY
const numeros = [];
console.log(numeros);

// Crear Array con valores
const colores = ["Amarillo", "Azúl", "Rojo"];
colores.reverse();
console.log(colores);

// Crear con valores iguales
const siete = new Array(4).fill(7);
console.log(siete);

// Añadir valor
siete.push(10);
siete.push(12);

// Eliminar valor
siete.shift();

for (let i = 0; i < siete.length; i++) {
    console.log(siete[i]);
}

// Mostrar parte del array
console.log(siete.slice(2, 4));

// Recorrer colores
for (color of colores) {
    // 
    console.log(color);
}

// Otra forma de recorrer Arrays
// Muestra el indice
for (i in colores) {
    // document.write(i);
    document.write(`</br>${i}.) ${colores[i]}</br>`)
}
