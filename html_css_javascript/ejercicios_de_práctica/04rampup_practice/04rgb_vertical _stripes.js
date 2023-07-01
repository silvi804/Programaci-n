// write your code here

function rgbImage(someImage) {
  var newImage = new SimpleImage(someImage);
  var width = newImage.getWidth() / 3;

  for (var pixel of newImage.values()) {
    if (pixel.getX() <= width) {
      pixel.setRed(255);
    } else if (pixel.getX() <= 2 * width) {
      pixel.setGreen(255);
    } else {
      pixel.setBlue(255);
    }
  }
  print(newImage);
}

rgbImage("hilton.jpg");

// go back to modifing images
