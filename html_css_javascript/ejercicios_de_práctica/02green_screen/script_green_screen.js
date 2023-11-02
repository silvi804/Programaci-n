var fgImage = null;
var bgImage = null;
var imgCanvas = null;
var imgCanvas2 = null;
function loadForeground() {
  imgCanvas = document.getElementById("c1");
  var fileinput = document.getElementById("fInput");
  fgImage = new SimpleImage(fileinput);
  fgImage.drawTo(imgCanvas);
}

function loadBackground() {
  imgCanvas2 = document.getElementById("c2");
  var fileinput2 = document.getElementById("bInput");
  bgImage = new SimpleImage(fileinput2);
  bgImage.drawTo(imgCanvas2);
}
function doClear(canvas) {
  var context = canvas.getContext("2d");
  context.clearRect(0, 0, canvas.width, canvas.height);
}

function clearCanvas() {
  doClear(imgCanvas);
  doClear(imgCanvas2);
}

function greenScreen() {
  if (fgImage == null || !fgImage.complete()) {
    alert("foreground not loaded");
  }
  if (bgImage == null || !bgImage.complete()) {
    alert("background not loaded");
  }
  var output = new SimpleImage(fgImage.getWidth(), fgImage.getHeight());
  for (var pixel of fgImage.values()) {
    var x = pixel.getX();
    var y = pixel.getY();
    if (pixel.getGreen() > 240 && pixel.getBlue() + pixel.getRed() < 100) {
      var bgPixel = bgImage.getPixel(x, y);
      output.setPixel(x, y, bgPixel);
    } else {
      output.setPixel(x, y, pixel);
    }
  }
  clearCanvas();
  output.drawTo(imgCanvas);
}
