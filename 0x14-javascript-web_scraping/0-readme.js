#!/usr/bin/node

const fs = require('fs');
const file = process.argv;

fs.readFile(file, 'utf8', function (err, line) {
  if (err) {
    console.error(err);
  } else {
  console.log(line);
  }
});
