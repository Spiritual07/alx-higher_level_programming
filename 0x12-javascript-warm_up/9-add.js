#!/usr/bin/node

function add (a, b) {
  const numA = parseInt(a);
  const numB = parseInt(b);
  let result;

  if (isNaN(numA) || isNaN(numB)) {
    console.log('NaN');
  } else {
    result = numA + numB;
    console.log(result);
  }
}
add(process.argv[2], process.argv[3]);
