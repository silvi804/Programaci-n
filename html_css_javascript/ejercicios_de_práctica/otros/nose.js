//Start with the foreground and background images you want (fgImage), (bgImage)
var fgImage = new SimpleImage("drewRobert.png");
var bgImage = new SimpleImage("dinos.png");
//A blan image of the same size(output)
var output = new SimpleImage(fgImage.getWidth(), fgImage.getHeight());

// for each pixel in fgImage
for (var pixel of fgImage.values()) {
  var x = pixel.getX();
  var y = pixel.getY();
  if (pixel.getGreen() > 0 && pixel.getBlue() === 0 && pixel.getRed() === 0) {
    var bgPixel = bgImage.getPixel(x, y);
    output.setPixel(x, y, bgPixel);
  } else {
    output.setPixel(x, y, pixel);
  }
}

print(output);
