#!/usr/bin/node

const convertedNumber = parseInt(process.argv[2]);
let lineCounter;

if (process.argv.length === 2 || isNaN(convertedNumber)) {
  console.log('Missing number of occurrences');
} else {
  for (lineCounter = 0; lineCounter < convertedNumber; lineCounter++) {
    console.log('C is fun');
  }
}
