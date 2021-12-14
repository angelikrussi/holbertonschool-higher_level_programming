#!/usr/bin/node
const nA = process.argv;
if (nA.length === 2) {
  console.log('No argument');
} else if (nA.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
