var a = 2;
var b = new Number(1);
var c = 7.19;
var d = "5.6";
console.log(
  c.toFixed(1), // redondea a número decimal inclusivo
  c.parseInt(), //develve solo la parte entera
  a.parseFloat() // devuelve la parte decimal
);

console.log(typeof c, typeof d);
console.log(c + d);

console.log(c + parseInt(d)); // depende del constuctor Number, por eso no viene de la forma d.__

console.log(parseInt("11", 2));
// Javascript no tiente tantos tipos de datos numéricos
// Es mejor trabajar con librerías para evitar errores numéricos
