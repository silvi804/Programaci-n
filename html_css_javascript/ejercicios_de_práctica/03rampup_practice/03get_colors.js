function printPixel(nameImage, xpos, ypos) {
  var someImg = new SimpleImage(nameImage);
  var pixelito = someImg.getPixel(xpos, ypos);
  const red = pixelito.getRed();
  const green = pixelito.getGreen();
  const blue = pixelito.getBlue();

  print(`red is ${red}`);
  print(`green is ${green}`);
  print(`blue is ${blue}`);
}

printPixel("drewgreen.png", 10, 10);
printPixel("drewgreen.png", 250, 500);
