// Trabajar con métodos más avanzados
// map(), filter(), reduce()
const array_1 = ["San Sebastian", "Madrid", "Barcelona", "Alicante", "Bilbaa"];

const val = array_1.forEach(v => {
    return 4;
});

console.log(val);

// map()
const newArray = array_1.map((valor, indice) => `${indice} ${valor}`);
console.log(newArray);

// filter()
const listaObjetos = [
    {nombre: "David", edad: 27},
    {nombre: "Patricia", edad: 50},
    {nombre: "Felipe", edad: 21},
    {nombre: "Andrés", edad: 27},
];

/* const personasMayores = listaObjetos.filter(obj => {
    if (obj.edad > 30) {
        return true;
    } else {
        return false;
    }
}); */

const personasMayores = listaObjetos.filter(obj => obj.edad > 30);
console.log(personasMayores);

const nuevaLista = listaObjetos.filter(o => o.nombre === "David");
console.log(nuevaLista);

// reduce()
const valores = [3, 56, 23, 5, 90, 100];

const suma = valores.reduce((acumulado, cur, i, arrayOriginal) => {
    console.log(acumulado);
    console.log(cur);
    console.log(i);
    console.log(arrayOriginal);

    return acumulado + cur;
});

console.log(suma);
