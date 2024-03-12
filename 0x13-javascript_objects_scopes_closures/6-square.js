#!/usr/bin/node
const Squarep = require('./5-square.js');

class Square extends Squarep {
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
