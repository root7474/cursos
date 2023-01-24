// Crear array
const numeros = [];
console.log(numeros);

// Crear con valores
const colores = ['rojo', 'amarillo', 'verde', 'marron'];
colores.reverse();
console.log(colores);

// Crear con valores iguales
const seis = new Array(4).fill(6);
console.log(seis);

// Añdir valor
seis.push(10);
seis.push(12);

// Eliminar valor
seis.shift();

// Mostrar
for (let i = 0; i < seis.length; i++) {
    console.log(seis[i]);
}


// Mostrar parte del array
console.log(seis.slice(2, 4));

// Recorrer colores
for (color of colores) {
    console.log(color);
}

// Otra forma de recorrer arrays
// Muestra el indice
for (i in colores) {
    // document.write(i);
    document.write(`<br/>${i}.) ${colores[i]}<br/>`)
}
