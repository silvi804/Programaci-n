function changeRed(width, height, verde, azul) {
  var picture = new SimpleImage(width, height);
  var red = 0;
  var verde = verde;
  var azul = azul;
  // for (var pixel of img.values())
  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      var pixelito = picture.getPixel(x, y);
      var rojito = x;
      pixelito.setRed(rojito);
      pixelito.setGreen(verde);
      pixelito.setBlue(azul);
    }
  }

  return picture;
}

var result = changeRed(256, 200, 0, 0);
print(result);

var result2 = changeRed(256, 200, 100, 200);
print(result2);
