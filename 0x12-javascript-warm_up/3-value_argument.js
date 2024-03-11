#!/usr/bin/node

if (process.argv[2] !== undefined && process.argv[3] === undefined) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
