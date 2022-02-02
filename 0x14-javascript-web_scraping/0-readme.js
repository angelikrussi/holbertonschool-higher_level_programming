#!/usr/bin/node

const fs = require('fs');
const File = process.argv[2];
fs.readFile(File, 'utf8', function(err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
