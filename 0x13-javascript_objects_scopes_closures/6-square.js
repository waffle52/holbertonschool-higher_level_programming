#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let letter;
    let i;
    let j;
    let test = '';
    if (typeof c !== 'undefined') {
      letter = c;
    } else {
      letter = 'X';
    }
    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        test = test.concat(letter);
      }
      console.log(test);
      test = '';
    }
  }
}

module.exports = Square;
