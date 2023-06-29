const arreglito = [];

const c = Array.of("x", "y");

const d = Array(100).fill(false); // iincializar múltiples posiciones con un valor

const colores = ["rojo", "verde", "azul"];
colores.push("NegRO"); //agrega un color al final

colores.pop(); // elimina el último elemento de una función
colores.shift(); // elimina el primer elemento de una función

colores.unshift("Happy");
colores.forEach(function (el, index) {
  console.log(<li id="${index}">${el}</li>); // ejecuta una función para cada elemento del arreglo
});

// ${valor} no solo es para comillas
