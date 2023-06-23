// Ambito global
var hola = "Hola Mundo"
// objeto window, scope global en navegadores
console.log(window.hola)
// Ambito de bloque
let hello = "Hello World"
console.log(window.hello)

// Ejemplo
// Usando siempre var
console.log("****************var*****************");
var musica = "Rock";
console.log("Variable Música antes del Bloque", musica);
{
    var musica = "Pop";
    console.log("Variable Música dentro del Bloque", musica);
}
console.log("Variable Música después del Bloque", musica);

// Aplicando let

console.log("****************let*****************");
let musica2 = "Rock";
console.log("Variable Música antes del Bloque", musica2);
{
    let musica2 = "Pop";
    console.log("Variable Música dentro del Bloque", musica2);
}
console.log("Variable Música después del Bloque", musica2);
