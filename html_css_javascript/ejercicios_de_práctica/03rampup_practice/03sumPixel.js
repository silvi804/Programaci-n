function sumPixel(nameOfImage, xpos, ypos) {
  var someImg = new SimpleImage(nameOfImage);
  var pixelito = someImg.getPixel(xpos, ypos);
  const red = pixelito.getRed();
  const green = pixelito.getGreen();
  const blue = pixelito.getBlue();
  var total = red + green + blue;
  return total;
}

var answer = sumPixel("drewgreen.png", 250, 500);
print(answer);
answer = sumPixel("drewgreen.png", 10, 10);
print(answer);
