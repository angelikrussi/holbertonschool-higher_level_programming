#!/usr/bin/node
const nA = process.argv[2];
if (!nA) {
  console.log('Not a number');
} else if (parseInt(nA)) {
  console.log('My number: ' + Math.floor(nA));
} else {
  console.log('Not a number');
}
