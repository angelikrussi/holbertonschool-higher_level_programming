#!/usr/bin/node

const fs = require('fs');
const Filefirst = process.argv[2];
const Filesecond = process.argv[2];

fs.writeFile(Filefirst, Filesecond, function (err, data) {
  if (err) {
    console.log(err);
  }
});
