// // image to highest red posible

var img = new SimpleImage("chapel.png");

for (var pixel of img.values()) {
  pixel.setRed(255);
}

print(img);

// image to lowest red posible

for (var pixel of img.values()) {
  pixel.setRed(0);
}

print(img);

// imaage to less red

var image = new SimpleImage("eastereggs.jpg");
for (var pixel of image.values()) {
  if (pixel.getRed() > 70) {
    pixel.setRed(70);
  }
}

print(image);
