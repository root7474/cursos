let altura_centimetros = 169;
let altura_metros = altura_centimetros / 100;
let peso = 59.8;
let altura_redondeada = Math.ceil(altura_metros);
let peso_redondeado = Math.floor(peso);
let max_1 = Number.MAX_VALUE + 1;
let max_2 = Number.MAX_VALUE;

console.log(altura_centimetros);
console.log(altura_metros);
console.log(peso);
console.log(altura_redondeada);
console.log(peso_redondeado);
console.log(max_1);
console.log(max_2);

if (max_1 === max_2) {
    console.log(`${max_1} y ${max_2} son iguales.`);
} else {
    console.log(`${max_1} y {max_2} no son iguales.`);
}
