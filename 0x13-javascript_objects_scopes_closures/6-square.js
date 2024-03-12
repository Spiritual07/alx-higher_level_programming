#!/usr/bin/node
const SquareK = require('./5-square.js');

class Square extends SquareK {
  charPrint (c) {
    for (let x = 0; x < this.height; x++) {
      let row = '';
      for (let y = 0; y < this.width; y++) {
        if (c === undefined) {
          row += 'x';
        } else {
          row += 'c';
        }
      }
      console.log(row);
    }
  }
}

module.exports = Square;
