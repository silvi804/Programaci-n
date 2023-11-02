var image = new SimpleImage("duke_blue_devil.png");
var w = image.getWidth();
var h = image.getHeight();

for (var pixel of image.values()) {
  if (
    pixel.getBlue() == 255 &&
    pixel.getGreen() == 255 &&
    pixel.getRed() == 255
  ) {
    continue;
  } else {
    pixel.setRed(0);
  }
  pixel.setGreen(255);
  pixel.setBlue(100);
}

print(image);
