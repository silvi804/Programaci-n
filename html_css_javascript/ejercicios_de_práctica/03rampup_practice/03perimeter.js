function perimeter(imageName) {
  var someImg = new SimpleImage(imageName);
  var w = someImg.getWidth();
  var h = someImg.getHeight();

  perim = 2 * w + 2 * h - 2;
  return perim;
}

print(perimeter("rodger.png"));
