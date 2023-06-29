// Add Thick Black Line to Bottom of Owen
var image = new SimpleImage("astrachan.jpg");
var w = image.getWidth();
var h = image.getHeight();

for (var pixel of image.values()) {
  if (pixel.getY() > h - 11) {
    pixel.setRed(0);
    pixel.setGreen(0);
    pixel.setBlue(0);
  }
}

print(image);

// cGreen square in top left corner
var image2 = new SimpleImage("chapel.png");

for (var pixel of image2.values()) {
  if (pixel.getX() <= 49) {
    if (pixel.getY() <= 49) {
      pixel.setRed(0);
      pixel.setGreen(255);
      pixel.setBlue(0);
    }
  }
}
print(image2);

//Rectangle of any color in top right corner

function topRightCorner(
  cornerWidth,
  cornerHeight,
  someImage,
  red,
  green,
  blue
) {
  var newImage = new SimpleImage(someImage);
  for (var pixel of newImage.values()) {
    if (pixel.getX() >= newImage.getWidth() - cornerWidth) {
      if (pixel.getY() < cornerHeight) {
        pixel.setRed(red);
        pixel.setGreen(green);
        pixel.setBlue(blue);
      }
    }
  }
  return newImage;
}

var picture = new SimpleImage("chapel.png");
var result = topRightCorner(30, 60, picture, 255, 255, 0);
print(result);
var picture2 = new SimpleImage("smalllion.jpg");
var result2 = topRightCorner(125, 20, picture2, 255, 0, 0);
print(result2);
