var image;
function upload() {
  var imgCanvas = document.getElementById("c1");
  var fileinput = document.getElementById("fInput");
  image = new SimpleImage(fileinput);
  image.drawTo(imgCanvas);

  image2 = new SimpleImage(fileinput);
  for (var pixel of image2.values()) {
    var avg = (pixel.getRed() + pixel.getGreen() + pixel.getBlue()) / 3;
    pixel.setRed(avg);
    pixel.setGreen(avg);
    pixel.setBlue(avg);
  }
  var imgCanvas2 = document.getElementById("c2");
  image2.drawTo(imgCanvas2);
}

// function makeGray() {
// pretende que se vuelva gris pero hay problemas con la librería así que aceptaré mi realidad jsjsj

// }
