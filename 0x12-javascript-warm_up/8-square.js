#!/usr/bin/node

const convertedNumber = parseInt(process.argv[2]);
let x;
let y;

if (process.argv.length === 2 || isNaN(convertedNumber)) {
  console.log('Missing size');
} else {
  for (x = 0; x < convertedNumber; x++) {
    let row = '';
    for (y = 0; y < convertedNumber; y++) {
      row += 'X';
    }
    console.log(row);
  }
}
