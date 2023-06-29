function rangeOfNumbers(startNum, endNum) {
  if (endNum < startNum) {
    return [];
  } else {
    var arr = rangeOfNumbers(startNum, endNum - 1);
    arr.push(endNum);
    return arr;
  }
}
console.log(rangeOfNumbers(1, 5));
