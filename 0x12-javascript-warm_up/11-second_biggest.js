#!/usr/bin/node
const lA = process.argv.length;
if (lA < 4) {
  console.log('0');
} else {
  const num = process.argv.sort((a, b) => a - b);
  console.log(num[num.length - 2]);
}
