#!/usr/bin/node
const lA = process.argv[2];
if (!lA) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < lA; x++) {
    console.log('C is fun');
  }
}
