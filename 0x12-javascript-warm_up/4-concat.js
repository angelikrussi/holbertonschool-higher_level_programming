#!/usr/bin/node
const cA = process.argv;
if (!cA) {
  console.log('No argument');
} else {
  console.log(cA[2] + ' is ' + cA[3]);
}
