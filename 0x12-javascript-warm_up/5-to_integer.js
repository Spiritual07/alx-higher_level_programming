#!/usr/bin/node

const convertedNumber = parseInt(process.argv[2]);
if (process.argv.length === 2 || isNaN(convertedNumber)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convertedNumber);
}
