// para usar carateres especiales
const sampleStr = 'Alan said, "Peter is learning JavaScript".';
// string escape sequences
/*

 \'	single quote
\"	double quote
\\	backslash
\n	newline
\t	tab
\r	carriage return
\b	backspace
\f	form feed

 */

// construcor, poco utilizado
let wenas = new String("Un objeto String");
let nombre = "Consuela";
let lorem_ipsum =
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus varius ut augue sit amet ultricies. Quisque nec sodales sem. Sed pretium eleifend metus ac pellentesque. Ut ac arcu odio. Praesent nec lacus et metus semper porttitor a a ex. Donec faucibus, nisi a convallis faucibus, eros nunc finibus ipsum, nec hendrerit leo nisl a felis. Suspendisse ut elit sapien.";
console.log(
  //propiedad
  nombre.length(), //longitud
  //método
  nombre.toUpperCase(), //mayúscula
  nombre.toLowerCase(), //minúscula
  lorem_ipsum.includes("amet"),
  lorem_ipsum.includes("wenas"), // True y False si incluye o no la cadena
  lorem_ipsum.trim(), //quita espacios en blancos del inicio y del final
  lorem.split(" ") // separa por lo que le asigné y lo vuelve un arreglo
);

//concatenar

var primer_nombre = "consuela";
var apellido = "fallangi";

var phoebe = " my name is " + nombre + " " + apellido + ".";
console.log(phoebe);

// interpolación de variables
//Template Stirng
var phoebe2 = `My name is ${primer_nombre} ${apellido}.`;
console.log(phoebe2);

// permite saltos de línea

var wow = `
 +saslkas a 
 esto es la forma de poner varias líneas
 lo vuelve sencillo
 debería usarse siempre
 
`;
