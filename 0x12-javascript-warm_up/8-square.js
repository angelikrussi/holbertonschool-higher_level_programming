#!/usr/bin/node
const lA = process.argv[2];
if (parseInt(lA)) {
  for (let x = 0; x < lA; x++) {
    console.log('X'.repeat(lA));
  }
} else {
  console.log('Missing size');
}
