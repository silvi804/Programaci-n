function numberPixels(namefile) {
  var someImg = new SimpleImage(namefile);
  var height = someImg.getHeight();
  var width = someImg.getWidth();
  totalNumber = height * width;
  return totalNumber;
}

var result = numberPixels("chapel.png");
print(result);
result = numberPixels("dinos.png");
print(result);
