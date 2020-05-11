#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    let j;
    let test = '';
    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        test = test.concat('X');
      }
      console.log(test);
      test = '';
    }
  }
}

module.exports = Rectangle;
