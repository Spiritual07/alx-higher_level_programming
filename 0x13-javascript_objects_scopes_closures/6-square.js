#!/usr/bin/node
const SquareP = require('./5-square.js');

class Square extends SquareP {
  charPrint (c) {
    for (let x = 0; x < this.height; x++) {
      let row = '';
      for (let y = 0; y < this.width; y++) {
        if (c === undefined) {
          row += 'X';
        } else {
          row += 'c';
        }
      }
      console.log(row);
    }
  }
}

module.exports = Square;
